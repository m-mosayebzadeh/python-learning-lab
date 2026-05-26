import parser
import analyzer
import plotter

from pathlib import Path

path = Path(__file__).parent.parent / "data" / "log_2days.txt"

df = parser.parse_logs(path)

plotter.plot_log_types(analyzer.get_log_type_count(df))