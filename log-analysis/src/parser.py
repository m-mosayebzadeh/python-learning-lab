import re
import pandas as pd

def parse_to_csv(filename):

    date = []
    time = []
    date_time = []
    level = []
    message = []

    with open(filename, "r") as f:
        reg = re.compile(r"^(\d{4}-\d{2}-\d{2})\s(\d{2}:\d{2}:\d{2})\s(ERROR|WARN|INFO)\s(.+)$")
        for l in f.readlines():
            a = re.match(reg, l)
            
            if a:
                date.append(a.group(1))
                time.append(a.group(2))
                date_time.append(pd.to_datetime(a.group(1) + " " + a.group(2)))
                level.append(a.group(3))
                message.append(a.group(4))
    
    df = pd.DataFrame()

    return df.from_dict({
        "datetime":date_time,
        "date":date,
        "time":time,
        "level":level,
        "message":message
    })