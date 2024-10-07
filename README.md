# AutoFair

## First time setup

```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements/dev.txt   
```

## Testing with coverage

```bash
    python3 -m coverage run -m unittest tests/tests_Utils.py
    python3 -m coverage report 
```

### Produce coverage report in json format

```bash
    python3 -m coverage json
```

### Exclude files from coverage report

Add the following line inline with the code to exclude it from the coverage report.

```none
    # pragma: no cover 
```

### Produce annotated source code for each file

```bash
    python3 -m coverage annotate
```


KISS Decisions for now:
- no [poetry](https://python-poetry.org/) (package manager) for now
