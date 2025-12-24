import mailbox
import pandas as pd
import re
from email.utils import parsedate_to_datetime

def load_mbox(path):
    rows = []

    for msg in mailbox.mbox(path):
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    payload = part.get_payload(decode=True)
                    if payload:
                        body += payload.decode(errors="ignore")
        else:
            payload = msg.get_payload(decode=True)
            if payload:
                body = payload.decode(errors="ignore")

        try:
            date = parsedate_to_datetime(msg.get("date"))
        except Exception:
            date = None

        rows.append({
            "from": msg.get("from", ""),
            "subject": msg.get("subject", ""),
            "date": date,
            "body": body.strip()
        })

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"], errors="coerce", utc=True)

    # derived fields
    df["hour"] = df["date"].dt.hour
    df["weekday"] = df["date"].dt.day_name()
    df["length"] = df["body"].str.len()
    df["opening"] = df["body"].str.split("\n").str[0].str.strip()

    # sender display
    def sender_display(s):
        if not s:
            return "Unknown"
        m = re.search(r'"?([^"<]+?)"?\s*<', s)
        if m:
            return m.group(1).strip()
        if "@" in s:
            return s.split("@")[0].replace(".", " ").title()
        return s

    df["sender"] = df["from"].apply(sender_display)

    return df
