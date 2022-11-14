########################################################################
# Makefile to automate common tasks
#
# Targets:
#
# build-venv - (re)build the Python virtual environment if needed
# test - run the unit tests (building a virtual environment if needed)
########################################################################


# activation script for the Python virtual environment
VENV=venv/bin/activate

# run unit tests
test: $(VENV)
	. $(VENV) && python setup.py test

# alias to (re)build the Python virtual environment
build-venv: $(VENV)

# (re)build the virtual environment if it's missing, or whenever setup.py changes
$(VENV): setup.py
	rm -rf venv && python3 -m venv venv && . $(VENV) && python setup.py develop

# publish a new release on PyPi
publish-pypi: $(VENV)
	. $(VENV) && pip install twine && rm -rf dist/* && python setup.py sdist && twine upload dist/*

# end

