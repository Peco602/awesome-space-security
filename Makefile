install:
	pip install -r requirements.txt

toc:
	md_toc -p -s 1 github README.md

copy: toc
	cp $(CURDIR)/README.md $(CURDIR)/docs/index.md

preview: copy
	mkdocs serve

build: copy
	mkdocs build

deploy: copy
	mkdocs gh-deploy --clean
