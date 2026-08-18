# 📅 CalSync — Smart Calendar Agent & Live Schedule Hub

An automated RFC 5545 calendar generator, email dispatcher, and live `webcal://` subscription hub built for **Apple Calendar (iOS / macOS)**, **Google Calendar**, and **Microsoft Outlook**.

---

## 🚀 Quick Start for Subscribers (Live `webcal://` Feed)

You can subscribe directly to live-updating schedules without downloading files manually.

### On iPhone / iPad / Mac (Apple Calendar):
1. Copy the `webcal://` feed link:
   ```text
   webcal://lsaacd.github.io/CalSync/2026%20Fall%20Semester/Fall_2026_All_Classes_Combined.ics
   ```
2. Open Safari on iPhone and paste the URL, or go to **Settings $\rightarrow$ Calendar $\rightarrow$ Accounts $\rightarrow$ Add Account $\rightarrow$ Other $\rightarrow$ Add Subscribed Calendar**.
3. Set **Auto-Refresh** to **Every Hour**.
4. All classes, labs, and exams will appear on your phone and automatically stay updated whenever the repository changes!

### On Google Calendar (Web):
1. Go to [Google Calendar](https://calendar.google.com).
2. Next to **Other calendars**, click **+ $\rightarrow$ From URL**.
3. Paste:
   ```text
   https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/Fall_2026_All_Classes_Combined.ics
   ```

---

## 🛠️ Automated Agent Setup (For Contributors & Developers)

The included Python agent parses calendar events, builds RFC 5545 `.ics` files, and automatically emails calendar invitations directly to your inbox with Apple Mail-compatible MIME headers.

### 1. Installation
Requires Python 3.10+ (uses only Python standard libraries, zero external dependencies required).

### 2. Configuration
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Generate a 16-character [Google App Password](https://myaccount.google.com/apppasswords).
3. Set your email and app password inside `.env`:
   ```env
   GMAIL_SENDER=your-email@gmail.com
   GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx
   GMAIL_RECIPIENT=your-email@gmail.com
   ```
*(Note: `.env` is ignored by git to keep your credentials 100% private).*

### 3. Usage
* **Dispatch a Single Event / Calendar File**:
  ```bash
  python send_ics.py "2026 Fall Semester/WRI 100 - Advanced Writing/WRI_100_02_Lecture.ics"
  ```
* **Dispatch an Entire Semester Folder (Batch)**:
  ```bash
  python send_ics.py "2026 Fall Semester"
  ```

---

## 📂 Project Structure

```
├── .env.example                               # Credential template (public-safe)
├── .gitignore                                 # Protects private .env and cache
├── AGENTS.md                                  # Complete agent architecture & SOP
├── send_ics.py                                # SMTP dispatcher & calendar packaging engine
└── 2026 Fall Semester/                        # Fall 2026 Semester schedules
    ├── README.md                              # Term dashboard & timetable
    ├── Fall_2026_All_Classes_Combined.ics     # One-tap master calendar feed
    ├── WRI 100 - Advanced Writing/
    ├── CSE 100 - Algorithm Design and Analysis/
    └── CSE 108 - Full Stack Web Development/
```

---

## 📜 RFC 5545 Compliance Features
* **Timezone Safety**: Native `VTIMEZONE` blocks for `America/Los_Angeles` prevent 1-hour shifts during Daylight Saving Time.
* **Granular Recurrence (`RRULE`)**: Weekly class recurrence terminates on the final day of instruction to eliminate phantom meetings during Finals Week.
* **Notification Alarms (`VALARM`)**: Pre-configured arrival and exam notifications.
