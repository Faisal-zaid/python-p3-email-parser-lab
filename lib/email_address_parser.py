import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        # Split on commas or spaces
        emails = re.split(r"[,\s]+", self.email_string.strip())

        # Remove empty strings
        emails = [email for email in emails if email]

        # Regex to validate an email address
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        # Keep only valid emails
        emails = [email for email in emails if re.match(email_pattern, email)]

        # Remove duplicates and sort
        unique_sorted = sorted(set(emails))

        return unique_sorted
