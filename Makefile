install:
	pip install -r requirements.txt

sort:
	python sort.py

copy: sort
	cp $(CURDIR)/README.md $(CURDIR)/docs/index.md

preview: copy
	mkdocs serve

build: copy
	mkdocs build

deploy: copy
	mkdocs gh-deploy --clean
