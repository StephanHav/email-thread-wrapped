import mailbox
import pandas as pd
from email.utils import parsedate_to_datetime

def load_mbox(path):
    rows = []
    for msg in mailbox.mbox(path):
        body = ""
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body += part.get_payload(decode=True).decode(errors="ignore")
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")

        rows.append({
            "from": msg.get("from"),
            "to": msg.get("to"),
            "cc": msg.get("cc"),
            "subject": msg.get("subject"),
            "date": parsedate_to_datetime(msg.get("date")),
            "body": body.strip()
        })

    return pd.DataFrame(rows)
