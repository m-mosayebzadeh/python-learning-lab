import re
import pandas as pd
from datetime import datetime

LOG_PATTERN = re.compile(r"^(?P<date>\d{4}-\d{2}-\d{2})\s(?P<time>\d{2}:\d{2}:\d{2})\s(?P<level>ERROR|WARN|INFO)\s(?P<message>.+)$")

def parse_logs(filename):

    rows = []

    with open(filename, "r") as f:

        for line in f:
            match = LOG_PATTERN.match(line)
            
            if match:
                rows.append({
                    "datetime":datetime.strptime((match.group("date") + " " + match.group("time")), "%Y-%m-%d %H:%M:%S"),
                    "level":match.group("level"),
                    "message":match.group("message")
                })

    return pd.DataFrame(rows)