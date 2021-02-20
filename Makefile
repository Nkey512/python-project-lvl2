install:
	poetry install
gendiffer:
	poetry run gendiff
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall
lint:
	poetry run flake8 gendiff tests
test:
	poetry run pytest gendiff tests
test2:
	poetry run pytest --cov=gendiff tests --cov-report xml
