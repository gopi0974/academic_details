# Student Performance Classification & Automated Report Generation System 🎓

An advanced, interactive, and beautiful academic evaluation system built with **Python**, **Pandas**, and **Streamlit**. It provides faculty with a secure portal to upload student grades, automatically classify student performance, visually inspect metrics, export styled color-coded spreadsheets, and dispatch dynamic HTML report card notifications.

---

## 🌟 Key Features

1. **Secure Faculty Portal**: Basic protected sign-in for faculty members.
2. **Column Validation**: Automatic scanning of uploaded Excel worksheets to guarantee required fields are fully clean.
3. **Double-Mid Slow Learner Mapping**:
   - Classifies slow learners individually for **Mid-1** and **Mid-2** (marks `< 10`).
   - Grouping combined overall averages into:
     - **High Performance (Fast Learners)**: Average Score `> 16`
     - **Medium Performance (Average Learners)**: Average Score `10 - 16`
     - **Low Performance (Slow Learners)**: Average Score `< 10`
4. **Rich Visual Analytics**:
   - Donut chart of overall performance distribution.
   - Dynamic Seaborn scatter plot mapping marks progression.
   - Grouped branch-wise evaluation comparisons.
   - Metric comparison bar charts.
5. **Styled Excel Reports**: Fully styled exported worksheets with freeze-panes, custom fonts, autowidth adjustments, and color-coded conditional cells using `openpyxl`.
6. **Automated SMTP Mailer**: Sends stunning responsive HTML emails to students (custom report cards, study recommendations) or detailed summaries with spreadsheet attachments to faculty.

---

## 📁 Modular Directory Structure

```text
student_report_system/
│
├── app.py                      # Core Streamlit Web Application Dashboard
├── requirements.txt            # Package Dependencies (pandas, openpyxl, seaborn, etc.)
├── README.md                   # Setup and User Guide (this file)
│
└── modules/
    ├── __init__.py             # Namespace package indicator
    ├── auth.py                 # Faculty Portal Authentication logic & Login UI
    ├── analyzer.py             # Data cleaning, column validation, classification logic
    ├── visualizer.py           # Seaborn & Matplotlib custom plotting
    ├── reporter.py             # OpenPyXL conditional formatting & styled Excel exporter
    ├── emailer.py              # SMTP SSL/TLS connection & HTML mailing service
    └── sample_template.py      # Test template generator with edge cases
```

---

## 🚀 Setup & Execution Instructions

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 2. Installation
Open your terminal in the project directory and install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Running the Application
Launch the Streamlit dashboard:
```bash
streamlit run app.py
```

Streamlit will automatically host the application and open it in your default web browser (typically at `http://localhost:8501`).

---

## 🔑 Portal Credentials (Demo evaluations)

To log into the Faculty dashboard for college mini-project evaluations, use either of these credentials:

| Portal Role | Username | Password |
| :--- | :--- | :--- |
| **Faculty Coordinator** | `faculty` | `password123` |
| **Academic Registry Admin** | `admin` | `admin2026` |

---

## 📂 Testing out of the Box

1. Launch the app and log in using `faculty` / `password123`.
2. Look at the **left sidebar** and click **⬇️ Download Sample Excel**. This downloads an Excel sheet populated with dummy data (including missing columns/grades to show off data recovery!).
3. Drag and drop that downloaded sample file into the main **Assessment Uploader** section.
4. Navigate through the tabs:
   - **Dashboard & Overview**: View the tabular records and download the styled Excel sheets.
   - **Detailed Classifications**: Drill down on Mid-1 and Mid-2 slow learners.
   - **Visual Analytics**: Beautiful graphs showing student distributions.
   - **Automated Emailer**: Configure your SMTP details to send real test emails.

---

## 🔒 Security Note on SMTP
For testing Gmail integration, standard passwords will block login. You must go to your **Google Account Settings ➔ Security ➔ 2-Step Verification**, and create an **App Password** to enter into the portal's SMTP Settings panel.
