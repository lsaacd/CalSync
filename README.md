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

## 🚀 Live Calendar Subscriptions (Individual Class Feeds)

You can subscribe to **individual classes, labs, and exams independently** on your iPhone, Mac, or Google Calendar so your schedule only includes the exact classes you want.

### 📱 How to Subscribe on iPhone / iPad / Mac:
1. Tap or copy any of the **`webcal://`** links in the table below.
2. In **Safari**, tap **Subscribe** $\rightarrow$ set **Auto-Refresh** to **Every Hour** (or Daily).
3. The individual class will now appear on your calendar and auto-update whenever changes occur!

### 💻 How to Subscribe on Google Calendar (Web):
1. Copy the **Google Calendar Feed URL** for any course below.
2. Go to [Google Calendar](https://calendar.google.com) $\rightarrow$ next to **Other calendars**, click **`+` $\rightarrow$ From URL** $\rightarrow$ paste link and click **Add calendar**.

---

### 📋 Fall 2026 Individual Live Feeds

| Course & Type | Day & Time | Location | 📱 Apple Calendar (`webcal://`) | 💻 Google Calendar Feed |
| :--- | :--- | :--- | :--- | :--- |
| **WRI 100-02**<br>*(Lecture)* | Tue & Thu<br>9:30 AM – 11:20 AM | Granite Pass 120 | [`Subscribe`](webcal://lsaacd.github.io/CalSync/2026%20Fall%20Semester/WRI%20100%20-%20Advanced%20Writing/WRI_100_02_Lecture.ics) | [`Feed URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/WRI%20100%20-%20Advanced%20Writing/WRI_100_02_Lecture.ics) |
| **CSE 100-01**<br>*(Lecture)* | Tue & Thu<br>9:00 PM – 10:15 PM | COB 1 Bldg 105 | [`Subscribe`](webcal://lsaacd.github.io/CalSync/2026%20Fall%20Semester/CSE%20100%20-%20Algorithm%20Design%20and%20Analysis/CSE_100_01_Lecture.ics) | [`Feed URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20100%20-%20Algorithm%20Design%20and%20Analysis/CSE_100_01_Lecture.ics) |
| **CSE 100-04L**<br>*(Lab)* | Wednesday<br>10:30 AM – 1:20 PM | S&E 1 Bldg 100 | [`Subscribe`](webcal://lsaacd.github.io/CalSync/2026%20Fall%20Semester/CSE%20100%20-%20Algorithm%20Design%20and%20Analysis/CSE_100_04L_Lab.ics) | [`Feed URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20100%20-%20Algorithm%20Design%20and%20Analysis/CSE_100_04L_Lab.ics) |
| **CSE 100-01**<br>*(Final Exam)* | Fri, Dec 18, 2026<br>11:30 AM – 2:30 PM | COB 1 Bldg 102 | [`Subscribe`](webcal://lsaacd.github.io/CalSync/2026%20Fall%20Semester/CSE%20100%20-%20Algorithm%20Design%20and%20Analysis/CSE_100_01_Final_Exam.ics) | [`Feed URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20100%20-%20Algorithm%20Design%20and%20Analysis/CSE_100_01_Final_Exam.ics) |
| **CSE 108-01**<br>*(Lecture)* | Thursday<br>4:00 PM – 6:20 PM | Remote Instruction | [`Subscribe`](webcal://lsaacd.github.io/CalSync/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_01_Lecture.ics) | [`Feed URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_01_Lecture.ics) |
| **CSE 108-05L**<br>*(Lab)* | Tuesday<br>4:30 PM – 7:20 PM | S&E 1 Bldg 100 | [`Subscribe`](webcal://lsaacd.github.io/CalSync/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_05L_Lab.ics) | [`Feed URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_05L_Lab.ics) |
| **CSE 108-01**<br>*(Midterm)* | Thu, Nov 19, 2026<br>5:00 PM – 6:20 PM | COB 2 Bldg 110 | [`Subscribe`](webcal://lsaacd.github.io/CalSync/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_01_Midterm_Exam.ics) | [`Feed URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_01_Midterm_Exam.ics) |
| **CSE 108-01**<br>*(Final Exam)* | Mon, Dec 14, 2026<br>6:30 PM – 9:30 PM | Remote Instruction | [`Subscribe`](webcal://lsaacd.github.io/CalSync/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_01_Final_Exam.ics) | [`Feed URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_01_Final_Exam.ics) |
| **⭐ All Classes & Exams**<br>*(Full Bundle)* | Full Semester | All Locations | [`Subscribe All`](webcal://lsaacd.github.io/CalSync/2026%20Fall%20Semester/Fall_2026_All_Classes_Combined.ics) | [`All Feed URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/Fall_2026_All_Classes_Combined.ics) |

---

## 🤖 Creating Your Own Class Schedule (Using an AI IDE)

Want to create calendar files for your **own university courses, labs, and exams**? You don't need to write `.ics` code manually!

This repository includes **[`AGENTS.md`](file:///c:/Users/isaac/Desktop/[02]%20WORK/[04]%20SCRIPTS%20&%20AGENTS/[03]%20ICS%20CALENDAR%20AGENT/AGENTS.md)**, which instructs AI coding assistants (such as **Google Antigravity**, **Cursor**, **Windsurf**, or **Claude Code**) to act as your autonomous calendar agent.

### How It Works:
1. **Fork or Clone this Repository**:
   ```bash
   git clone https://github.com/lsaacd/CalSync.git
   ```
2. **Open the Folder in Your AI IDE** (e.g., Google Antigravity, Cursor, or Windsurf).
3. **Paste Your Own Class Schedule Text into the AI Chat**:
   Copy the raw text from your university student portal (Ellucian Banner, Canvas, Workday, etc.) and prompt the AI:
   > *"Here is my class schedule for next semester. Generate individual .ics files and a combined live feed for my classes following the AGENTS.md standard."*
4. **The AI Agent will automatically**:
   * 📖 Read `AGENTS.md` to ensure strict RFC 5545 compliance and timezone settings.
   * 🗂️ Generate individual, titled `.ics` files for every lecture, lab, and discussion.
   * ⏰ Attach **3-tier countdown alarms** (1 day, 2 hours, 30 mins) to all midterms & final exams.
   * 🛑 Set weekly recurrence cutoffs to the last day of regular class instruction (preventing phantom meetings during finals week).
   * 📁 Structure your files into organized course folders and compile an updated schedule dashboard.
5. **Get Your Calendar Files & Import**:
   * **Drag & Drop to iCalendar**: Once the agent finishes, you can simply take your generated `.ics` files (or zip your new semester folder) and drag them directly into Apple Calendar on Mac or Google Calendar web.
   * **Import to iPhone**: If you're importing via iPhone, watch this helpful walkthrough:  
     📺 **[How to Import .ics Calendar Files to iPhone Calendar (YouTube Guide)](https://www.youtube.com/watch?v=xEaamiZDWuo)**
   * **Email Delivery**: Add your Gmail App Password to `.env` and tell the agent: *"Email these calendar invites to my iPhone."*

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
