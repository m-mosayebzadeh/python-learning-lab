# Log Analysis Lab 📊

A mini Python project for parsing, analyzing, and visualizing log files, built as part of my Python learning journey.

## Features

- Parse log files using Regex
- Convert logs into Pandas DataFrame
- Analyze log levels (ERROR / WARN / INFO)
- Count message frequency
- Analyze logs over time
- Generate charts with Matplotlib
- Expose analysis through FastAPI endpoints

---

## Project Structure

```text
log-analysis/
│
├── data/
│   └── log_2days.txt
│
├── output/
│
├── src/
│   ├── main.py
│   │
│   ├── api/
│   │   └── log_api.py
│   │
│   ├── core/
│   │   └── parser.py
│   │
│   └── services/
│       ├── analyzer.py
│       └── plotter.py
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/m-mosayebzadeh/python-learning-lab.git
cd log-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run API Server

```bash
python -m uvicorn src.main:app --reload
```

Open Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Available Endpoints

### Get log type counts

```text
GET /logs/count
```

Response:

```json
[
  {
    "level":"INFO",
    "count":3430
  },
  {
    "level":"ERROR",
    "count":1375
  }
]
```

---

### Get message frequency

```text
GET /logs/frequency
```

---

## Technologies

- Python
- FastAPI
- Pandas
- Matplotlib
- Regex

---