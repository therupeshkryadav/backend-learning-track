# Phase 0 — Python basics

This directory contains a small interactive Python script for learning basics:

- `myapp.py` — simple interactive script that asks for the user's name, age, favorite color, and weight in kilograms, then prints an estimated year of birth and the weight converted to pounds.

How to run

1. Activate a Python 3 virtual environment (recommended) or use the installed Python interpreter.
2. Run:

```bash
python phase-0-python-basics/myapp.py
```

Notes

- The year-of-birth calculation uses the current calendar year and assumes the user has already had their birthday this year; for exact results, ask for the full birth date.
- Weight is input in kilograms and converted to pounds (kg × 2.20462). The output is formatted to one decimal place for kilograms and two decimal places for pounds.
- This script is intentionally simple for learning; feel free to add input validation and extra prompts.
