POETRY = poetry

all: install

install:
	$(POETRY) install

test:
	$(POETRY) run pytest

format:
	$(POETRY) run black src tests

run_consumer:
	$(POETRY) run python src/event_consumer/run_consumer.py

run_propagator:
	$(POETRY) run python src/event_propagator/run_propagator.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	rm -rf .coverage htmlcov

.PHONY: all install test format run clean
