all: flake8 test

check-syntax-errors:
	python -m compileall -q .

clean-pyc:
	find . -name '*.pyc' -exec rm \{\} \;

ctags:
	ctags --recurse=yes .

flake8:
	@# Do not analyse .gitignored files.
	@# `make` needs `$$` to output `$`. Ref: http://stackoverflow.com/questions/2382764.
	flake8 `git ls-files | grep "\.py$$"`

test: check-syntax-errors
	nosetests openfisca_france_data/tests --ignore-files='(test_calibration.py|test_inflation.py|test_eipp.py|test_surveys.py|test_simulation.py|test_pivot_table.py|test_aggregates.py)' --exe --with-doctest
