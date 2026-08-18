# ICS Calendar Agent — Knowledge Base & Instructions (`AGENTS.md`)

## 1. Overview & Purpose
This repository houses the **ICS Calendar Agent**, an automated system designed to:
1. Parse natural language scheduling instructions or structured event data.
2. Generate strictly compliant **RFC 5545 (`.ics` / iCalendar)** calendar files.
3. Automatically dispatch calendar invites to the user's email (Gmail / Apple Mail) for seamless one-tap addition to iPhone/iOS Calendar, Google Calendar, and Microsoft Outlook.

---

## 2. Key Learnings & Technical Specifications

### A. The RFC 5545 iCalendar Standard
An `.ics` file is a plain-text file containing calendar objects structured into hierarchical blocks:

```text
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//ICS Calendar Agent//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VEVENT
UID:<unique-identifier>@domain.com
DTSTAMP:<utc-timestamp-of-creation>Z
DTSTART:<event-start>
DTEND:<event-end>
SUMMARY:<Event Title>
DESCRIPTION:<Event Details / Notes>
LOCATION:<Physical address or virtual URL>
STATUS:CONFIRMED
TRANSP:OPAQUE
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:<Reminder text>
TRIGGER:-PT15M
END:VALARM
END:VEVENT
END:VCALENDAR
```

#### Critical Property Rules:
* **`UID`**: Globally unique identifier (e.g., `YYYYMMDDTHHMMSSZ-hash@domain.com`). Essential for updates/deletions.
* **`DTSTAMP`**: Creation/modification timestamp in UTC (`YYYYMMDDTHHMMSSZ`).
* **All-Day Events**:
  * Format: `DTSTART;VALUE=DATE:YYYYMMDD`
  * **Exclusive `DTEND` rule**: `DTEND` must be set to the **next day** (e.g., for a 1-day event on Aug 19, `DTSTART=20260819` and `DTEND=20260820`).
* **Timed Events**:
  * UTC format: `DTSTART:20260819T140000Z`
  * Local/Floating format: `DTSTART:20260819T090000`
  * Explicit Timezone: `DTSTART;TZID=America/Los_Angeles:20260819T090000`
* **Recurrence (`RRULE`)**:
  * Weekly: `RRULE:FREQ=WEEKLY;BYDAY=TU` (e.g. Garbage pickup every Tuesday)
  * Bi-weekly: `RRULE:FREQ=WEEKLY;INTERVAL=2;BYDAY=TH`
  * Monthly: `RRULE:FREQ=MONTHLY;BYMONTHDAY=1`
* **Reminders (`VALARM`)**:
  * Negative duration trigger: `TRIGGER:-PT15M` (15 minutes prior), `TRIGGER:-PT1H` (1 hour prior), `TRIGGER:-P1D` (1 day prior).
* **Escaping & Formatting**:
  * Special characters `,`, `;`, and `\` in text fields (`SUMMARY`, `DESCRIPTION`, `LOCATION`) must be escaped with a backslash (`\,`, `\;`, `\\`).
  * Newlines in descriptions must be encoded as `\n`.
  * Lines longer than 75 octets should be folded with CRLF followed by a single space or tab.

---

### B. iOS & Mobile Calendar Workaround
* **The Problem**: When downloading `.ics` files directly via iOS Safari or saving them to the iOS Files app, iOS often does not present the native **"Add to Calendar"** sheet.
* **The Solution**: Emailing the `.ics` file as an attachment to an account linked to the native **Apple Mail** app.
* **MIME Configuration**:
  * Email header Content-Type: `text/calendar; charset="utf-8"; method=PUBLISH; name="event.ics"`
  * Content-Disposition: `attachment; filename="event.ics"`
  * Apple Mail natively parses the `text/calendar` attachment and displays a prominent **"Add to Calendar"** / **"Add All"** button in the footer.

---

### C. Individual File Creation Standard (Crucial Rule)
* **Granular Calendar Files**: Unless explicitly asked to combine events, **always generate a separate, dedicated `.ics` file for each distinct course, lecture, lab, discussion, midterm, or final exam**.
* **Rationale**:
  * Allows users to title, color-code, enable/disable, or delete individual classes and labs independently in Apple Calendar / Google Calendar.
  * Ensures clean event subjects and separate email notifications for each schedule item.
---

### D. Academic Calendar, Recurrence Boundaries & Timezones
* **Instruction Period vs. Finals Week**:
  * Regular lectures, labs, and discussions must use `RRULE:FREQ=WEEKLY;BYDAY=...;UNTIL=<end-of-instruction-UTC>` where `UNTIL` terminates on the **last day of regular class instruction** (e.g., Dec 11, 2026), **not** the end of final exam week.
  * **Final exams** must be scheduled as separate, standalone one-off events on their designated exam dates/times.
  * **Rationale**: Extending the regular lecture `UNTIL` date through finals week causes false "phantom" class meetings to show up during finals week when no classes are being held.
* **Multi-Tier Alarms for Exams**:
  * Regular classes and labs should include a standard 20-minute notification (`TRIGGER:-PT20M`).
  * Midterms and Final Exams must include a **3-tier alert hierarchy**:
    1. `TRIGGER:-P1D` (1 Day before — preparation alert)
    2. `TRIGGER:-PT2H` (2 Hours before — commute & packing alert)
    3. `TRIGGER:-PT30M` (30 Minutes before — arrival alert)
  * Set `CATEGORIES:Exams,Academics` and `PRIORITY:1` on all exam events.

---

## 3. Automation Architecture & Scripts

### Current Components:
* **[send_ics.py](file:///c:/Users/isaac/Desktop/[02]%20WORK/[04]%20SCRIPTS%20&%20AGENTS/[03]%20ICS%20CALENDAR%20AGENT/send_ics.py)**: Python SMTP sender supporting Gmail App Passwords, single/batch directory dispatching, and calendar MIME construction.
* **[parse_schedule.py](file:///c:/Users/isaac/Desktop/[02]%20WORK/[04]%20SCRIPTS%20&%20AGENTS/[03]%20ICS%20CALENDAR%20AGENT/parse_schedule.py)**: Intelligent registration portal and syllabus text parser that generates compliant `.ics` files and directory trees automatically.

### Configuration / Environment Variables:
The sender script can read credentials from environment variables to run in headless/agent mode:
* `GMAIL_SENDER`: Sender Gmail address.
* `GMAIL_APP_PASSWORD`: Google 16-character App Password.
* `GMAIL_RECIPIENT`: Destination email address (defaults to sender if omitted).

---

## 4. Agent Operating Workflow (SOP)

When the user asks to create or schedule a calendar event:

1. **Extract Event Details**:
   - Separate distinct courses/components (Lectures, Labs, Midterms, Final Exams).
   - Extract Title (`SUMMARY`), Date & Time (Start, End, Timezone), Recurrence (`RRULE`), Location, Instructors/CRN (`DESCRIPTION`), and Alarms (`VALARM`).
2. **Generate Individual Compliant ICS Files**:
   - Format each component as its own independent RFC 5545 `.ics` file.
   - Attach multi-tier alarms to all exams and 20-minute alarms to classes.
   - Write each `.ics` file to the workspace with descriptive filenames.
3. **Dispatch / Delivery**:
   - Run `send_ics.py <filename>.ics` (or folder) to deliver invites directly to the user's inbox.
4. **Verification**:
   - Provide a clear breakdown of each generated file and confirmation of dispatch.

