import pandas as pd
import core.parser as parser


def get_log_type_count() -> pd.Series:
    return parser.parse_logs()["level"].value_counts()

def get_log_frequency_by_level(level:str|None = None) -> pd.Series:

    data = parser.parse_logs()

    if level:
        data = data[data["level"] == level]

    return data["message"].value_counts()

def count_logs_by_time(unit:str = "h") -> pd.Series:

    data = parser.parse_logs()

    allowed_date = ["Y", "M"]
    allowed_time = [ "d", "h", "min"]

    if unit in allowed_time: 
        calc_way = data["datetime"].dt.floor(unit)
    elif unit in allowed_date:
        calc_way = data["datetime"].dt.to_period(unit)
    else:
        raise ValueError(f"Invalid time unit: {unit}")

    return data.groupby(calc_way).size()
