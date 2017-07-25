run:
	PYTHONPATH=. python containers/command.py

test:
	python -m unittest discover containers
