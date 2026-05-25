import parser
import analyze

from pathlib import Path

path = Path(__file__).parent.parent / "data" / "log_2days.txt"

df = parser.parse_logs(path)

print(analyze.get_log_type_count(df))
print(analyze.get_log_frequency_by_level(df, "ERROR"))
print(analyze.count_logs_by_time(df))