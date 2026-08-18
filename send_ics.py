import os
import re
import smtplib
import zipfile
from email.message import EmailMessage
from email.utils import formatdate, make_msgid
import sys

def load_dotenv(env_path: str = ".env"):
    """Simple parser to load key=value from .env without third-party dependencies."""
    if not os.path.exists(env_path):
        # Also check current file's directory
        env_path = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

def extract_summary_from_ics(ics_path: str) -> str:
    """Extracts the SUMMARY field from an ICS file if available."""
    try:
        with open(ics_path, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.search(r"^SUMMARY:(.+)$", content, re.MULTILINE)
        if match:
            return match.group(1).strip()
    except Exception:
        pass
    return "Calendar Event"

def send_calendar_email(
    ics_file_path: str,
    to_email: str = None,
    sender_email: str = None,
    sender_app_password: str = None,
    subject: str = None,
    body: str = None
):
    """
    Sends an .ics calendar file as an email attachment via Gmail SMTP.
    """
    load_dotenv()

    sender_email = sender_email or os.getenv("GMAIL_SENDER")
    sender_app_password = sender_app_password or os.getenv("GMAIL_APP_PASSWORD")
    to_email = to_email or os.getenv("GMAIL_RECIPIENT") or sender_email

    if not sender_email or not sender_app_password:
        raise ValueError("Sender email or App Password not provided in arguments or .env.")

    # Clean app password (remove spaces)
    sender_app_password = sender_app_password.replace(" ", "")

    if not os.path.exists(ics_file_path):
        # Also check relative to workspace directory
        alt_path = os.path.join(os.path.dirname(__file__), ics_file_path)
        if os.path.exists(alt_path):
            ics_file_path = alt_path
        else:
            print(f"[ERROR] Could not find file '{ics_file_path}'")
            return False

    summary = extract_summary_from_ics(ics_file_path)
    subject = subject or f"Calendar Event: {summary}"
    body = body or (
        f"Here is your calendar invite for '{summary}'.\n\n"
        f"Tap the attached calendar (.ics) file below or in Apple Mail to add it to your calendar with one click."
    )

    with open(ics_file_path, "r", encoding="utf-8") as f:
        ics_content = f.read()

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid()

    msg.set_content(body)

    # Attach ICS file with standard calendar MIME headers
    filename = os.path.basename(ics_file_path)
    msg.add_attachment(
        ics_content.encode("utf-8"),
        maintype="text",
        subtype="calendar",
        filename=filename,
        params={"method": "PUBLISH", "name": filename}
    )

    print(f"Connecting to Gmail SMTP server for {sender_email} -> {to_email}...")
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_app_password)
            server.send_message(msg)
        print(f"[SUCCESS] Successfully dispatched '{filename}' ({summary}) to {to_email}!")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")
        return False

def create_zip_archive(dir_path: str, output_zip_path: str = None) -> str:
    """Creates a zip file of a directory."""
    if output_zip_path is None:
        output_zip_path = os.path.join(os.path.dirname(dir_path), f"{os.path.basename(dir_path)}.zip")
    with zipfile.ZipFile(output_zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                file_full = os.path.join(root, file)
                rel_path = os.path.relpath(file_full, os.path.dirname(dir_path))
                zipf.write(file_full, rel_path)
    return output_zip_path

def dispatch_target(target_path: str, recipient: str = None):
    """Dispatches a single .ics file or all .ics files in a directory recursively."""
    if not os.path.exists(target_path):
        alt = os.path.join(os.path.dirname(__file__), target_path)
        if os.path.exists(alt):
            target_path = alt
        else:
            print(f"[ERROR] Path does not exist: {target_path}")
            return

    if os.path.isdir(target_path):
        ics_files = []
        for root, _, files in os.walk(target_path):
            for file in files:
                if file.lower().endswith(".ics"):
                    ics_files.append(os.path.join(root, file))
        if not ics_files:
            print(f"No .ics files found in '{target_path}'.")
            return
        print(f"Found {len(ics_files)} .ics files to dispatch...")
        for f in ics_files:
            send_calendar_email(ics_file_path=f, to_email=recipient)
    else:
        send_calendar_email(ics_file_path=target_path, to_email=recipient)

if __name__ == "__main__":
    load_dotenv()
    if len(sys.argv) < 2:
        print("Usage: python send_ics.py <path-to-ics-or-folder> [recipient-email]")
        sys.exit(1)

    target = sys.argv[1]
    target_to = sys.argv[2] if len(sys.argv) > 2 else None
    dispatch_target(target, target_to)
