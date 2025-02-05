import os
import json
import email
from email import policy
from datetime import datetime


def parse_eml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        msg = email.message_from_file(f, policy=policy.default)

    # Extract key fields
    email_data = {
        "timestamp": msg.get("Date", ""),
        "from": msg.get("From", ""),
        "to": msg.get("To", ""),
        "subject": msg.get("Subject", ""),
        "body": get_email_body(msg)
    }

    # Convert timestamp to standard format if possible
    try:
        parsed_date = email.utils.parsedate_to_datetime(
            email_data["timestamp"])
        email_data["timestamp"] = parsed_date.isoformat()
    except (TypeError, ValueError):
        pass

    return email_data


def get_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode(part.get_content_charset(), errors="ignore")
    else:
        return msg.get_payload(decode=True).decode(msg.get_content_charset(), errors="ignore")
    return ""


def process_eml_files(directory, output_file):
    emails = []

    for filename in os.listdir(directory):
        if filename.endswith(".eml"):
            file_path = os.path.join(directory, filename)
            email_data = parse_eml(file_path)
            emails.append(email_data)

    # Save as JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(emails, f, indent=4, ensure_ascii=False)

    print(f"Processed {len(emails)} emails and saved to {output_file}")


if __name__ == "__main__":
    # Change this to your directory containing .eml files
    input_directory = "./eml_files"
    output_json = "emails.json"
    process_eml_files(input_directory, output_json)
