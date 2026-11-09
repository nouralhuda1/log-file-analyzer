# Log File Analyzer

A Python-based log file analysis tool that reads, parses, analyzes, filters, and exports server log data.

## Features

- Read and process log files.
- Parse individual log entries into structured data.
- Validate log levels and HTTP status codes.
- Count log levels and HTTP status codes.
- Identify the most frequent IP addresses.
- Calculate successful and failed requests.
- Filter logs by level, IP address, and status code.
- Export reports in CSV and JSON formats.
- Interactive command-line menu.
- Basic file error handling.

## Technologies Used

- Python 3
- CSV
- JSON
- Collections (Counter)

## Project Structure

```text
log-file-analyzer/
│
├── analyzer/
│   ├── __init__.py
│   ├── reader.py
│   ├── parser.py
│   ├── statistics.py
│   └── exporter.py
│
├── data/
│   └── sample.log
│
├── reports/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/nouralhuda1/log-file-analyzer.git
```

2. Navigate into the project folder:

```bash
cd log-file-analyzer
```

3. Run the application:

```bash
python3 main.py
```

## Usage

After running the application, choose an option from the interactive menu:

1. View analysis report.
2. Filter logs.
3. Export reports.
4. Exit.

The application supports exporting all log entries or filtered results into CSV and JSON files.

Generated reports are saved in the `reports/` directory.

## Sample Analysis

The analyzer provides:

- Total number of log entries.
- Distribution of log levels.
- HTTP status code statistics.
- Top IP addresses.
- Successful and failed request counts.

## Future Improvements

- Support for additional log formats.
- Date and time-based filtering.
- Graphical data visualization.
- Automated report generation.

## Author

Nour
Software Engineering Student
