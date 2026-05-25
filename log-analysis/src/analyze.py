import pandas as pd


def get_log_type_count(data:pd.DataFrame) -> pd.Series:
    return data["level"].value_counts()

def get_log_frequency_by_level(data:pd.DataFrame, level:str|None = None) -> pd.Series:

    if level:
        data = data[data["level"] == level]

    return data["message"].value_counts()

def count_logs_by_time(data:pd.DataFrame, unit:str) -> pd.Series:

    allowed_date = ["Y", "M"]
    allowed_time = [ "d", "h", "min"]

    if unit in allowed_time: 
        calc_way = data["datetime"].dt.floor(unit)
    elif unit in allowed_date:
        calc_way = data["datetime"].dt.to_period(unit)
    else:
        raise ValueError(f"Invalid time unit: {unit}")

    return data.groupby(calc_way).size()
