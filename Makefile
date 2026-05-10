PYTHON = .venv/bin/python

.PHONY: venv install test run validate clean

venv:
	python3 -m venv .venv

install: venv
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e ".[dev]"

test:
	$(PYTHON) -m pytest

run:
	$(PYTHON) -m uvicorn app.main:app --host 127.0.0.1 --port 8000

validate:
	/home/sanek/projects/codex/paas/.venv/bin/python -m deployer.cli validate .

clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type d -name .pytest_cache -prune -exec rm -rf {} +
	find . -type d -name "*.egg-info" -prune -exec rm -rf {} +
