# 📅 CalSync

> **Smart RFC 5545 Calendar Engine, Live Subscription Hub & Automated Schedule Parser**  
> *Built for Apple Calendar (iOS / macOS), Google Calendar, and Microsoft Outlook.*

[![RFC 5545 Compliant](https://img.shields.io/badge/RFC_5545-Compliant-brightgreen.svg)](#-rfc-5545-compliance-features)
[![iOS & Apple Mail Ready](https://img.shields.io/badge/iOS_&_Apple_Mail-Ready-blue.svg)](#-quick-start-for-subscribers)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-yellow.svg)](#-automated-agent--developer-setup)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](#)

---

## 🎯 Why CalSync?

Adding university course schedules and exam dates to your phone is usually painful:
* ❌ Student portals (Ellucian Banner, Canvas, MyUCMerced) output messy schedules with separate exam pages.
* ❌ Downloading `.ics` files on iPhone Safari fails to prompt the native *"Add to Calendar"* dialog.
* ❌ Static calendar imports don't update when a professor moves a room or shifts a lecture to Zoom.

**CalSync solves all of this:**
1. **Live `webcal://` Syncing**: Subscribe once on iPhone or Google Calendar. Any room change or syllabus update pushed to GitHub automatically updates your phone in the background.
2. **100% Offline & Airplane Mode Ready**: The entire schedule is cached directly in your device memory—alarms and rooms show up even without Wi-Fi or cellular service.
3. **Smart Multi-Tier Alarms**: 20-minute reminders for normal lectures, plus **1-day, 2-hour, and 30-minute countdown alerts** for Midterms and Final Exams.
4. **Automated Schedule Parser**: Feed raw text from any student portal or syllabus to generate clean, individual `.ics` files in 2 seconds.

---

## 🚀 Live Calendar Subscription (No App Needed)

Subscribe directly on your phone to get live schedules that automatically update.

### 📱 On iPhone / iPad / Mac (Apple Calendar)
1. Copy the live feed URL:
   ```text
   webcal://lsaacd.github.io/CalSync/2026%20Fall%20Semester/Fall_2026_All_Classes_Combined.ics
   ```
2. Open **Safari** and paste the link (or go to **Settings $\rightarrow$ Calendar $\rightarrow$ Accounts $\rightarrow$ Add Account $\rightarrow$ Other $\rightarrow$ Add Subscribed Calendar**).
3. Set **Auto-Refresh** to **Every Hour** (or Daily) and tap **Add**.

### 💻 On Google Calendar (Web)
1. Open [calendar.google.com](https://calendar.google.com).
2. On the left sidebar next to **Other calendars**, click **`+` $\rightarrow$ From URL**.
3. Paste:
   ```text
   https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/Fall_2026_All_Classes_Combined.ics
   ```
4. Click **Add calendar**.

### 📥 Manual Import (Download ZIP & Drag to iCalendar / Apple Calendar)
If you prefer to download the repository and import files directly:
1. Click **Code $\rightarrow$ Download ZIP** on GitHub and extract the folder.
2. Drag and drop any individual `.ics` file (or `Fall_2026_All_Classes_Combined.ics`) directly into your Apple Calendar or Google Calendar app.
3. 📺 **Watch Video Walkthrough**: [How to Import .ics Calendar Files to iPhone Calendar (YouTube Guide)](https://www.youtube.com/watch?v=xEaamiZDWuo)

---

## ✨ Key Features

| Feature | What It Does | Why It Matters |
| :--- | :--- | :--- |
| 🔔 **Multi-Tier Exam Alarms** | Alerts at **1 Day before**, **2 Hours before**, and **30 Mins before** for all exams. | Never get caught off guard on exam morning. |
| 🤖 **Smart Schedule Parser** | Extracts courses, CRNs, instructors, and rooms from raw portal text. | Turn messy portal registrations into clean `.ics` files instantly. |
| 🌐 **Timezone & DST Safe** | Full `America/Los_Angeles` `VTIMEZONE` embedding. | Times never shift by 1 hour when Daylight Saving Time ends in November. |
| 🛑 **Recurrence Boundaries** | Regular weekly lectures automatically cut off on the last day of instruction. | Eliminates "phantom" class reminders during Finals Week. |
| ✉️ **One-Tap Apple Mail Invites** | Sends `.ics` attachments formatted with `text/calendar; method=PUBLISH`. | Renders native *"Add All"* action sheets inside iOS Mail. |

---

## 📋 Active Timetable: Fall 2026 Semester

| Course | Component | Days & Times | Location | Instructors / CRN |
| :--- | :--- | :--- | :--- | :--- |
| **WRI 100-02** | Lecture | **Tue & Thu** 9:30 AM – 11:20 AM | Granite Pass 120 | Catherine Koehler / Samantha Almeida (`31623`) |
| **CSE 100-01** | Lecture | **Tue & Thu** 9:00 PM – 10:15 PM | COB 1 Bldg 105 | Miguel Carreira-Perpiñán (`30378`) |
| **CSE 100-04L** | Lab | **Wednesday** 10:30 AM – 1:20 PM | S&E 1 Bldg 100 | Rasul Kairgeldin (`30859`) |
| **CSE 100-01** | **FINAL EXAM** | **Fri, Dec 18, 2026** 11:30 AM – 2:30 PM | COB 1 Bldg 102 | Miguel Carreira-Perpiñán (`30378`) |
| **CSE 108-01** | Lecture | **Thursday** 4:00 PM – 6:20 PM | Remote Instruction | Ammon Hepworth / Weimin Qiu (`31032`) |
| **CSE 108-05L** | Lab | **Tuesday** 4:30 PM – 7:20 PM | S&E 1 Bldg 100 | Weimin Qiu (`31294`) |
| **CSE 108-01** | **MIDTERM** | **Thu, Nov 19, 2026** 5:00 PM – 6:20 PM | COB 2 Bldg 110 | Ammon Hepworth / Weimin Qiu (`31032`) |
| **CSE 108-01** | **FINAL EXAM** | **Mon, Dec 14, 2026** 6:30 PM – 9:30 PM | Remote Instruction | Ammon Hepworth / Weimin Qiu (`31032`) |

---

## 🤖 Creating Your Own Class Schedule (Using an AI IDE)

Want to set up your own university classes, labs, and exams? You don't need to build `.ics` files manually!

This repository includes a comprehensive **[`AGENTS.md`](file:///c:/Users/isaac/Desktop/[02]%20WORK/[04]%20SCRIPTS%20&%20AGENTS/[03]%20ICS%20CALENDAR%20AGENT/AGENTS.md)** rulebook that guides AI coding assistants and IDEs (such as **Google Antigravity**, **Cursor**, **Windsurf**, or **Claude Code**) to act as your autonomous calendar scheduling agent.

### Step-by-Step:
1. **Fork or Clone this Repository**:
   ```bash
   git clone https://github.com/lsaacd/CalSync.git
   ```
2. **Open the Folder in Your AI IDE** (e.g., Antigravity, Cursor, or Windsurf).
3. **Paste Your Class Schedule Text into the AI Chat**:
   Copy the raw text from your university registration portal (Ellucian Banner, Canvas, Workday, etc.) and ask:
   > *"Here is my class schedule for next semester. Create individual .ics files and a combined live feed following the AGENTS.md standard."*
4. **The AI Assistant will automatically**:
   * 📖 Read `AGENTS.md` to ensure strict RFC 5545 compliance and timezone definitions.
   * 🗂️ Generate individual, color-coded `.ics` files for every lecture, lab, and discussion.
   * ⏰ Attach **3-tier countdown alarms** to midterms and final exams (1 day, 2 hours, 30 mins).
   * 🛑 Set weekly recurrence cutoffs to the last day of regular class instruction (preventing phantom meetings during finals week).
   * 📁 Structure your files into organized course folders and compile an updated schedule dashboard.
5. **(Optional) One-Tap Email Dispatch**:
   Add your Gmail App Password to `.env` and prompt:
   > *"Email these calendar invites to my iPhone."*

---

## 🛠️ CLI & Developer Tools

CalSync also includes standalone Python tools written with **zero third-party dependencies**.

### 1. Quick Setup
```bash
# Clone the repository
git clone https://github.com/lsaacd/CalSync.git
cd CalSync

# (Optional) Configure Gmail credentials for automated email dispatch
cp .env.example .env
# Add your Gmail App Password inside .env
```

### 2. Parse Raw Portal Text into Calendar Files
Turn raw text from your student portal or syllabus into `.ics` files:
```bash
python parse_schedule.py schedule_input.txt --folder "2026 Fall Semester" --email
```

### 3. Dispatch Calendar Files via Email
Send one-tap calendar invites to your iPhone inbox:
```bash
# Send a single class
python send_ics.py "2026 Fall Semester/WRI 100 - Advanced Writing/WRI_100_02_Lecture.ics"

# Send all classes in a semester folder
python send_ics.py "2026 Fall Semester"
```

---

## 📂 Repository Structure

```
CalSync/
├── .env.example                               # Safe credential template for developers
├── .gitignore                                 # Protects private .env credentials and archives
├── AGENTS.md                                  # Complete agent architecture & SOP standards
├── parse_schedule.py                          # Smart schedule & syllabus parser CLI
├── send_ics.py                                # RFC 5545 MIME email sender & batch dispatcher
└── 2026 Fall Semester/                        # Active semester schedules
    ├── README.md                              # Term timetable dashboard
    ├── Fall_2026_All_Classes_Combined.ics     # Master live-feed bundle
    ├── WRI 100 - Advanced Writing/
    ├── CSE 100 - Algorithm Design and Analysis/
    └── CSE 108 - Full Stack Web Development/
```

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
