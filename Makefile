install:
	sudo apt install ruby
	sudo gem install awesome_bot
	pip install -r requirements.txt

check_urls:
	awesome_bot README.md --allow-ssl -a 302,429 -w xbmc/xbmc

sort:
	python sort.py

toc:
	md_toc -p -s 1 github -l 2 README.md

copy: sort toc
	cp $(CURDIR)/README.md $(CURDIR)/docs/index.md

preview: copy
	mkdocs serve

build: copy
	mkdocs build

deploy: copy
	mkdocs gh-deploy --clean
