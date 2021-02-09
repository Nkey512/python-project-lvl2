install:
	poetry install
gendiffer:
	poetry run gendiff
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 gendiff
test:
	poetry run pytest --cov=gendiff tests/ --cov-report xml 4059a470293daa7f5bf04afd99081b4437c9ed86554c43aece8d1005ab5f3dae
