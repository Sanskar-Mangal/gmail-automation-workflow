# Step 1: Directly extract from JSON root
items = [
    {
        "json": {
            "Subject": "Meeting Reminder",
            "From": "hr@example.com",
            "snippet": "This is a gentle reminder about the meeting scheduled at 3 PM."
        }
    }
]

summary = items[0]["json"].get("Subject", "")
from_ = items[0]["json"].get("From", "")
email_body = items[0]["json"].get("snippet", "")

result = [
    {
        "json": {
            "summary": summary,
            "email_body": email_body,
            "from": from_
        }
    }
]

print(result)
