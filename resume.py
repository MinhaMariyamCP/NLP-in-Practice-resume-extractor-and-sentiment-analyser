import re
import json

resumes = [
    "Email: test@gmail.com Phone: +91-9876543210",
    "Contact: 9876543211 Email: user@yahoo.com",
    "Mail: abc@outlook.com Phone: 919876543210"
]

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}'
phone_pattern = r'(?:\+91[-\s]?|91[-\s]?)?[6-9]\d{9}'

results = []

for i, resume in enumerate(resumes):
    emails = re.findall(email_pattern, resume)
    phones = re.findall(phone_pattern, resume)

    results.append({
        "Resume": i+1,
        "Emails": emails,
        "Phones": phones
    })

with open("output.json", "w") as f:
    json.dump(results, f, indent=4)

print("Done ✅ Check output.json")