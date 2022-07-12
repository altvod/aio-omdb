build:
	rm -rf dist
	python -m build

upload:
	python -m twine upload --repository pypi dist/*

test:
	pytest tests
	mypy src/aio_omdb
