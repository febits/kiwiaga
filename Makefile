SRC=kiwiaga

.PHONY: all
all: black isort pylint

.PHONY: black
black:
	-poetry run black $(SRC)

.PHONY: isort
isort:
	-poetry run isort $(SRC)

.PHONY: pylint
pylint:
	-poetry run pylint $(SRC)
