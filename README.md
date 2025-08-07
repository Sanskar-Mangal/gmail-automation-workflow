# Gmail Automation Workflow using No-Code & Python

🚀 Automate your inbox to extract subject, sender, body, and action items from incoming emails, and save them directly to Google Sheets.

## ✨ Features
- Gmail Trigger-based automation
- Extracts key fields: Subject, Sender, Email Body, and Action Items
- Automatically appends extracted data into Google Sheets
- Built using n8n, Python (via Function node), and Google Sheets API

## 📸 Workflow Preview
![Workflow Screenshot](./assets/workflow-screenshot.png)

## 🧠 Logic Overview
- Extract headers and body from the Gmail payload
- Decode base64-encoded content
- Use regex or pattern-matching to extract action items
- Append structured output to a Google Sheet row

## 📁 Files Included
- workflow.json – Full workflow exported from n8n
- code/extract-email-data.py – Python code for parsing Gmail data
- docs/GmailAutomationDocumentation.pdf – Stakeholder-ready documentation

## 🔧 Tools & Technologies
- Gmail API (via n8n Gmail Trigger)
- Google Sheets Node in n8n
- Python for processing email content
- Base64 decoding, Regex, and conditional logic
- No-code automation via n8n.io

## 🧩 Future Enhancements
- Use LangChain, LLMs, or GPT to smartly extract action items
- Smart tagging and auto-responses
- Email classification using ML or AI
- Dashboard/report generation using Power BI

## 💼 About Me
I am a Full Stack Developer (React, Node.js, Python, .NET) transitioning into the AI field, with a passion for building efficient automation workflows and real-world productivity tools.

## 🔗 Connect With Me
- LinkedIn: https://www.linkedin.com/in/sanskar-mangal/
- Portfolio: https://sanskarmangal-portfolio.netlify.app/
- GitHub: https://github.com/Sanskar-Mangal