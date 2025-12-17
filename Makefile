VENV = venv
PYTHON = $(VENV)/bin/python
RUFF = $(VENV)/bin/ruff

.PHONY: lint test run 

lint:
	$(PYTHON) -m mypy .
	$(RUFF) check .

test: 
	$(PYTHON) -m pytest .

run:
	$(PYTHON) day1.py
	$(PYTHON) day2.py

