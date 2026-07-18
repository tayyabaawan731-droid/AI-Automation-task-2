# Security Log Parser

## Overview

This project is a Python command-line tool that parses security log files and extracts useful information into a CSV file. It is developed as part of THE ARZENS Engineering Internship Program – Beginner Track Assignment 2.

## Features

* Reads security log files from the command line
* Extracts timestamp, source IP, event type, and status
* Normalizes timestamps
* Exports parsed data to a CSV file
* Skips malformed log entries
* Displays a processing summary
* Supports `--dry-run` mode
* Handles file and permission errors gracefully

## Requirements

* Python 3.x

## How to Run

Run the parser:

```bash
python log_parser.py sample_logs.txt
```

Run in dry-run mode:

```bash
python log_parser.py sample_logs.txt --dry-run
```

## Output

The parser generates:

* `output_parsed.csv`

It also displays:

* Total lines processed
* Successful records
* Skipped records
* Output file name

## Project Files

* `log_parser.py`
* `sample_logs.txt`
* `output_parsed.csv`
* `README.md`
