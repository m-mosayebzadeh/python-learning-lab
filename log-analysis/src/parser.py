import re
import pandas as pd
from datetime import datetime

def parse_to_csv(filename):

    raws = []

    with open(filename, "r") as f:
        reg = re.compile(r"^(\d{4}-\d{2}-\d{2})\s(\d{2}:\d{2}:\d{2})\s(ERROR|WARN|INFO)\s(.+)$")

        for l in f:
            match = reg.match(l)
            
            if match:
                raws.append({
                    "datetime":datetime.strptime((match.group(1) + " " + match.group(2)), "%Y-%m-%d %H:%M:%S"),
                    "date":match.group(1),
                    "time":match.group(2),
                    "level":match.group(3),
                    "message":match.group(4)
                })

    return pd.DataFrame(raws)