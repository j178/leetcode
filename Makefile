new:
	python3 ./helper/new.py


push:
	git add .
	git commit
	git push

default: new

.PHONY: new push default