# Date Teller

A small Python script that converts dates in a text file from `DD-MM-YYYY` format to `YYYY-MM-DD` format.

## What it does

`dateteller.py` reads a text file (`dates.txt`), finds all dates written as `DD-MM-YYYY`, and converts them to `YYYY-MM-DD` using a regular expression.

**Example input** (`dates.txt`):
```
Today is 01-10-2025 and tomorrow is 02-10-2025.
Project deadline: 15-12-2025.
```

**Example output:**
```
Today is 2025-10-01 and tomorrow is 2025-10-02.
Project deadline: 2025-12-15.
```

## Files

- `dateteller.py` — main script
- `dates.txt` — input text file containing dates to convert

## Requirements

- Python 3 (uses only the standard library — `re` module)

## Usage

1. Make sure `dates.txt` is in the same directory as `dateteller.py`.
2. Run the script:

```bash
python dateteller.py
```

3. The converted text will be printed to the console:

```
Converted text    =    Today is 2025-10-01 and tomorrow is 2025-10-02.
Project deadline: 2025-12-15.
```

## How it works

The script uses this regex pattern to match dates:

```python
r'\b(\d{2})-(\d{2})-(\d{4})\b'
```

It captures the day, month, and year as separate groups, then rearranges them into `YYYY-MM-DD` order using `re.sub`:

```python
re.sub(date_pattern, r'\3-\2-\1', text)
```
