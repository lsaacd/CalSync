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

## 📋 Live Example Feeds: Fall 2026 Semester (Demo)

> [!NOTE]
> **Example Schedule:** The links in this section are live demonstration feeds for a sample UC Merced Fall 2026 computer science & writing schedule.  
> 👉 **To generate live feeds for YOUR OWN university classes**, jump to [Creating Your Own Class Schedule with an AI IDE](#-creating-your-own-class-schedule-using-an-ai-ide) below!

You can test how live subscriptions work by tapping any link below on your iPhone, Mac, or Google Calendar:

### 📱 How to Subscribe on iPhone / iPad / Mac:
1. Tap or copy any of the **Direct Calendar Feed links** in the table below (opens in Safari or Calendar).
2. When the iOS **Subscription Details** screen appears:
   * ⚠️ **IMPORTANT**: Turn **OFF** the toggle for **"Remove Alerts"** (toggle to Grey). If left green, iOS will block the exam countdown alarms and class reminders!
   * Set **Auto-Refresh** to **Every Hour** (or Daily).
3. Tap **Add** / **Done**. The class will now appear on your calendar and auto-update in the background!

### 💻 How to Subscribe on Google Calendar (Web):
1. Copy the **Feed URL** for any course below.
2. Go to [Google Calendar](https://calendar.google.com) $\rightarrow$ next to **Other calendars**, click **`+` $\rightarrow$ From URL** $\rightarrow$ paste link and click **Add calendar**.

---

### 📅 Fall 2026 Demo Feeds

| Course & Type | Day & Time | Location | 📱 Apple / iOS Calendar Link | 💻 Google Calendar Feed URL |
| :--- | :--- | :--- | :--- | :--- |
| **WRI 100-02**<br>*(Lecture)* | Tue & Thu<br>9:30 AM – 11:20 AM | Granite Pass 120 | [`Subscribe to WRI 100`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/WRI%20100%20-%20Advanced%20Writing/WRI_100_02_Lecture.ics) | [`Copy URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/WRI%20100%20-%20Advanced%20Writing/WRI_100_02_Lecture.ics) |
| **CSE 100-01**<br>*(Lecture)* | Tue & Thu<br>9:00 PM – 10:15 PM | COB 1 Bldg 105 | [`Subscribe to CSE 100 Lecture`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20100%20-%20Algorithm%20Design%20and%20Analysis/CSE_100_01_Lecture.ics) | [`Copy URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20100%20-%20Algorithm%20Design%20and%20Analysis/CSE_100_01_Lecture.ics) |
| **CSE 100-04L**<br>*(Lab)* | Wednesday<br>10:30 AM – 1:20 PM | S&E 1 Bldg 100 | [`Subscribe to CSE 100 Lab`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20100%20-%20Algorithm%20Design%20and%20Analysis/CSE_100_04L_Lab.ics) | [`Copy URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20100%20-%20Algorithm%20Design%20and%20Analysis/CSE_100_04L_Lab.ics) |
| **CSE 100-01**<br>*(Final Exam)* | Fri, Dec 18, 2026<br>11:30 AM – 2:30 PM | COB 1 Bldg 102 | [`Subscribe to CSE 100 Final Exam`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20100%20-%20Algorithm%20Design%20and%20Analysis/CSE_100_01_Final_Exam.ics) | [`Copy URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20100%20-%20Algorithm%20Design%20and%20Analysis/CSE_100_01_Final_Exam.ics) |
| **CSE 108-01**<br>*(Lecture)* | Thursday<br>4:00 PM – 6:20 PM | Remote Instruction | [`Subscribe to CSE 108 Lecture`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_01_Lecture.ics) | [`Copy URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_01_Lecture.ics) |
| **CSE 108-05L**<br>*(Lab)* | Tuesday<br>4:30 PM – 7:20 PM | S&E 1 Bldg 100 | [`Subscribe to CSE 108 Lab`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_05L_Lab.ics) | [`Copy URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_05L_Lab.ics) |
| **CSE 108-01**<br>*(Midterm)* | Thu, Nov 19, 2026<br>5:00 PM – 6:20 PM | COB 2 Bldg 110 | [`Subscribe to CSE 108 Midterm`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_01_Midterm_Exam.ics) | [`Copy URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_01_Midterm_Exam.ics) |
| **CSE 108-01**<br>*(Final Exam)* | Mon, Dec 14, 2026<br>6:30 PM – 9:30 PM | Remote Instruction | [`Subscribe to CSE 108 Final Exam`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_01_Final_Exam.ics) | [`Copy URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/CSE%20108%20-%20Full%20Stack%20Web%20Development/CSE_108_01_Final_Exam.ics) |
| **⭐ Master Bundle**<br>*(All Combined)* | Full Semester | All Locations | [`Subscribe All Classes & Exams`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/Fall_2026_All_Classes_Combined.ics) | [`Copy URL`](https://raw.githubusercontent.com/lsaacd/CalSync/main/2026%20Fall%20Semester/Fall_2026_All_Classes_Combined.ics) |

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
6. **(Optional) Host Your Own Live `webcal://` Feeds**:
   Push your generated files to your own GitHub repository and enable **GitHub Pages** in Repository Settings. You and your classmates can now subscribe to your custom live feed at:
   ```text
   webcal://<YOUR-USERNAME>.github.io/<YOUR-REPO>/<YOUR-SEMESTER-FOLDER>/...
   ```

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
