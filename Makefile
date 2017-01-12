# First thing first: run 'make buildout'
# then, activate the venv by running 'source venv/bin/activate'
buildout:
	[ -e venv/bin/python ] || virtualenv venv
	./venv/bin/pip install -r requirements.txt

# test:
    # TODO

clean:
	find . -name "*.pyc" | xargs rm -rf
	find . -name "*.pyo" | xargs rm -rf

realclean: clean
	find . -name "*.egg-info" | xargs rm -rf
	rm -rf .Python venv
