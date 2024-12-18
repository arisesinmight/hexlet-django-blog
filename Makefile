fix-imports:
	uv run ruff check --fix --select I
run:
	python manage.py runserver
