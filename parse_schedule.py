"""
==============================================================================
CalSync — Intelligent Schedule & Syllabus Parser (RFC 5545)
==============================================================================
Parses raw registration portal text, syllabi, or OCR dumps from Banner/Canvas,
generates individual & combined .ics calendar files, and optionally emails them.
==============================================================================
"""

import argparse
import datetime
import os
import re
import sys
import uuid

base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, base_dir)

VTIMEZONE_PACIFIC = [
    "BEGIN:VTIMEZONE",
    "TZID:America/Los_Angeles",
    "X-LIC-LOCATION:America/Los_Angeles",
    "BEGIN:DAYLIGHT",
    "TZOFFSETFROM:-0800",
    "TZOFFSETTO:-0700",
    "TZNAME:PDT",
    "DTSTART:19700308T020000",
    "RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=2SU",
    "END:DAYLIGHT",
    "BEGIN:STANDARD",
    "TZOFFSETFROM:-0700",
    "TZOFFSETTO:-0800",
    "TZNAME:PST",
    "DTSTART:19701101T020000",
    "RRULE:FREQ=YEARLY;BYMONTH=11;BYDAY=1SU",
    "END:STANDARD",
    "END:VTIMEZONE"
]

DAY_MAP = {
    "monday": "MO", "mon": "MO", "m": "MO",
    "tuesday": "TU", "tue": "TU", "tu": "TU", "t": "TU",
    "wednesday": "WE", "wed": "WE", "w": "WE",
    "thursday": "TH", "thu": "TH", "th": "TH", "r": "TH",
    "friday": "FR", "fri": "FR", "f": "FR",
    "saturday": "SA", "sat": "SA", "s": "SA",
    "sunday": "SU", "sun": "SU"
}

def parse_time_str(time_str: str) -> tuple:
    """Parses '09:30 AM' or '9:30am' into (hour, minute) in 24h format."""
    clean = time_str.strip().upper()
    match = re.search(r"(\d{1,2}):(\d{2})\s*(AM|PM)", clean)
    if not match:
        raise ValueError(f"Unable to parse time: '{time_str}'")
    hr = int(match.group(1))
    mn = int(match.group(2))
    period = match.group(3)
    if period == "PM" and hr < 12:
        hr += 12
    elif period == "AM" and hr == 12:
        hr = 0
    return hr, mn

def parse_date_str(date_str: str) -> datetime.date:
    """Parses 'MM/DD/YYYY' or 'YYYY-MM-DD'."""
    clean = date_str.strip()
    for fmt in ("%m/%d/%Y", "%Y-%m-%d", "%m-%d-%Y", "%m/%d/%y"):
        try:
            return datetime.datetime.strptime(clean, fmt).date()
        except ValueError:
            pass
    raise ValueError(f"Unable to parse date: '{date_str}'")

def escape_ics(text: str) -> str:
    """Escapes special characters for RFC 5545 text fields."""
    if not text:
        return ""
    return text.replace("\\", "\\\\").replace(",", "\\,").replace(";", "\\;").replace("\n", "\\n")

def create_event_ics(
    output_path: str,
    cal_name: str,
    summary: str,
    description: str,
    location: str,
    start_dt: datetime.datetime,
    end_dt: datetime.datetime,
    rrule: str = None,
    is_exam: bool = False,
    tzid: str = "America/Los_Angeles"
):
    """Writes a single RFC 5545 .ics file with appropriate single or multi-tier alarms."""
    now_stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    uid = f"{uuid.uuid4().hex[:12]}@calsync.local"
    dtstart_str = start_dt.strftime("%Y%m%dT%H%M%S")
    dtend_str = end_dt.strftime("%Y%m%dT%H%M%S")

    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//CalSync//Smart Schedule Parser//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        f"X-WR-CALNAME:{cal_name}",
        f"X-WR-TIMEZONE:{tzid}"
    ] + VTIMEZONE_PACIFIC

    lines.append("BEGIN:VEVENT")
    lines.append(f"UID:{uid}")
    lines.append(f"DTSTAMP:{now_stamp}")
    lines.append(f"DTSTART;TZID={tzid}:{dtstart_str}")
    lines.append(f"DTEND;TZID={tzid}:{dtend_str}")
    if rrule:
        lines.append(f"RRULE:{rrule}")
    lines.append(f"SUMMARY:{escape_ics(summary)}")
    lines.append(f"DESCRIPTION:{escape_ics(description)}")
    lines.append(f"LOCATION:{escape_ics(location)}")
    lines.append("STATUS:CONFIRMED")
    lines.append("TRANSP:OPAQUE")

    if is_exam:
        lines.append("CATEGORIES:Exams,Academics")
        lines.append("PRIORITY:1")
        # Multi-tier alarms for exams: 1 day, 2 hours, 30 mins
        lines.append("BEGIN:VALARM")
        lines.append("ACTION:DISPLAY")
        lines.append(f"DESCRIPTION:Exam Tomorrow: {escape_ics(summary)}")
        lines.append("TRIGGER:-P1D")
        lines.append("END:VALARM")
        lines.append("BEGIN:VALARM")
        lines.append("ACTION:DISPLAY")
        lines.append(f"DESCRIPTION:Exam in 2 Hours: {escape_ics(summary)}")
        lines.append("TRIGGER:-PT2H")
        lines.append("END:VALARM")
        lines.append("BEGIN:VALARM")
        lines.append("ACTION:DISPLAY")
        lines.append(f"DESCRIPTION:Exam in 30 Mins: {escape_ics(summary)}")
        lines.append("TRIGGER:-PT30M")
        lines.append("END:VALARM")
    else:
        lines.append("CATEGORIES:Lecture,Academics")
        lines.append("BEGIN:VALARM")
        lines.append("ACTION:DISPLAY")
        lines.append(f"DESCRIPTION:Reminder: {escape_ics(summary)}")
        lines.append("TRIGGER:-PT20M")
        lines.append("END:VALARM")

    lines.append("END:VEVENT")
    lines.append("END:VCALENDAR")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\r\n".join(lines) + "\r\n")

    print(f"Generated: {os.path.basename(output_path)}")
    return output_path

def parse_schedule_text(raw_text: str, output_folder: str = "Parsed_Schedule") -> list:
    """Intelligently extracts course sections and schedules from raw text."""
    target_dir = os.path.join(base_dir, output_folder)
    os.makedirs(target_dir, exist_ok=True)
    created_files = []

    # Regex patterns
    course_header_pattern = re.compile(
        r"\[?([^\|\n\]]+)\]?(?:\(https?://[^\)]+\))?\s*\|\s*([^\|\n]+)\s*\|\s*Class Begin:\s*([0-9/]+)\s*\|\s*Class End:\s*([0-9/]+)",
        re.IGNORECASE
    )
    meeting_pattern = re.compile(
        r"([0-9/]+)\s*--\s*([0-9/]+)\s+([A-Za-z, ]+)\s+(?:[SMTWRFS\s\n]+)?"
        r"([0-9]{1,2}:[0-9]{2}\s*(?:AM|PM))\s*-\s*([0-9]{1,2}:[0-9]{2}\s*(?:AM|PM))\s+Type:\s*([A-Za-z]+)\s+Location:\s*([^\n]+)",
        re.IGNORECASE
    )
    crn_pattern = re.compile(r"CRN:\s*([0-9]+)", re.IGNORECASE)
    instructor_pattern = re.compile(r"Instructor:\s*([^\n]+)", re.IGNORECASE)

    # Split text into course chunks
    chunks = course_header_pattern.split(raw_text)
    if len(chunks) < 5:
        # Single block or fallback
        print("Note: Parsing single-block or unstructured schedule text...")
    
    # Iterate through matched course blocks
    i = 1
    while i < len(chunks):
        title = chunks[i].strip()
        code_sec = chunks[i+1].strip()
        class_begin = chunks[i+2].strip()
        class_end = chunks[i+3].strip()
        body = chunks[i+4] if (i+4) < len(chunks) else ""
        i += 5

        crn_match = crn_pattern.search(body)
        crn = crn_match.group(1) if crn_match else "N/A"

        inst_match = instructor_pattern.search(body)
        instructor = inst_match.group(1).replace("[", "").replace("]", "") if inst_match else "Staff"

        # Sanitize folder and code names
        clean_code = re.sub(r"[^\w\s-]", "", code_sec).strip()
        course_folder = os.path.join(target_dir, f"{clean_code}")
        os.makedirs(course_folder, exist_ok=True)

        for meet in meeting_pattern.finditer(body):
            m_start_date_str = meet.group(1)
            m_end_date_str = meet.group(2)
            days_str = meet.group(3).strip()
            start_time_str = meet.group(4)
            end_time_str = meet.group(5)
            m_type = meet.group(6).strip()
            loc = meet.group(7).strip()

            start_d = parse_date_str(m_start_date_str)
            end_d = parse_date_str(m_end_date_str)
            s_hr, s_mn = parse_time_str(start_time_str)
            e_hr, e_mn = parse_time_str(end_time_str)

            is_exam = "exam" in m_type.lower() or "midterm" in m_type.lower() or "final" in m_type.lower()
            is_single = (start_d == end_d) or is_exam

            # Find first meeting datetime
            start_dt = datetime.datetime.combine(start_d, datetime.time(s_hr, s_mn))
            end_dt = datetime.datetime.combine(start_d, datetime.time(e_hr, e_mn))

            rrule = None
            if not is_single:
                bydays = []
                for d in re.split(r"[,/ ]+", days_str):
                    if d.lower() in DAY_MAP:
                        bydays.append(DAY_MAP[d.lower()])
                byday_str = ",".join(dict.fromkeys(bydays))
                # UNTIL formatted in UTC
                until_dt = datetime.datetime.combine(end_d, datetime.time(23, 59, 59))
                until_utc = (until_dt + datetime.timedelta(hours=7)).strftime("%Y%m%dT%H%M%SZ")
                rrule = f"FREQ=WEEKLY;UNTIL={until_utc};BYDAY={byday_str}"

            ev_summary = f"{clean_code}: {title} ({m_type.upper() if is_exam else m_type.title()})"
            ev_desc = (
                f"Course: {clean_code} - {title}\n"
                f"Type: {m_type}\n"
                f"CRN: {crn}\n"
                f"Instructor: {instructor}\n"
                f"Schedule: {days_str} {start_time_str} - {end_time_str}\n"
                f"Dates: {m_start_date_str} - {m_end_date_str}"
            )

            file_suffix = f"{m_type.replace(' ', '_')}"
            out_name = f"{clean_code.replace(' ', '_')}_{file_suffix}.ics"
            out_file = os.path.join(course_folder, out_name)

            fpath = create_event_ics(
                output_path=out_file,
                cal_name=ev_summary,
                summary=ev_summary,
                description=ev_desc,
                location=loc,
                start_dt=start_dt,
                end_dt=end_dt,
                rrule=rrule,
                is_exam=is_exam
            )
            created_files.append(fpath)

    print(f"\nSuccessfully parsed and generated {len(created_files)} calendar files in '{output_folder}'.")
    return created_files

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CalSync Schedule & Syllabus Parser")
    parser.add_argument("file_or_text", nargs="?", help="Path to schedule text file or raw text string")
    parser.add_argument("--folder", default="Parsed_Schedule", help="Output directory name")
    parser.add_argument("--email", action="store_true", help="Automatically dispatch generated files to email")
    args = parser.parse_args()

    if not args.file_or_text:
        print("Usage: python parse_schedule.py <schedule-file.txt> [--folder <out-dir>] [--email]")
        sys.exit(1)

    raw_input = ""
    if os.path.exists(args.file_or_text):
        with open(args.file_or_text, "r", encoding="utf-8") as f:
            raw_input = f.read()
    else:
        raw_input = args.file_or_text

    generated = parse_schedule_text(raw_input, output_folder=args.folder)

    if args.email and generated:
        from send_ics import send_calendar_email
        print("\nDispatching parsed calendar events to your email...")
        for gf in generated:
            send_calendar_email(gf)
