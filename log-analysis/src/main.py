import parser

from pathlib import Path

path = Path(__file__).parent.parent / "data" / "log_2days.txt"

print(parser.parse_to_csv(path))