VENV = venv
PYTHON = $(VENV)/bin/python
RUFF = $(VENV)/bin/ruff

.PHONY: lint test test-full run 

lint:
	$(PYTHON) -m mypy .
	$(RUFF) check .

# Don't run the large, slow tests
test: 
	$(PYTHON) -m pytest -v -m "not large" .

test-full: 
	$(PYTHON) -m pytest -v .

run:
	#$(PYTHON) day1.py
	#$(PYTHON) day2.py
	$(PYTHON) day3.py
