.PHONY: lint pylint isort yapf pydocstyle lint-fix bulid
all: build

rebuild: clean all

lint: pylint isort yapf cpplint clang-format pydocstyle
	echo "Success!"

pylint:
	pylint --rcfile=./.pylintrc .

isort:
	isort . --settings-path=./pyproject.toml -c --show-files

yapf:
	yapf --style ./pyproject.toml --recursive -d --verbose .

pydocstyle:
	pydocstyle --add-ignore=D107,D401,D104,D100,D105 --verbose .

lint-fix:
	isort . --settings-path=./pyproject.toml --show-files
	yapf --style ./pyproject.toml --recursive -i --verbose .

build:
	python3 -m pip install -r requirements.txt

clean:
	find . -type d -name __pycache__ -exec rm -r {} \+
