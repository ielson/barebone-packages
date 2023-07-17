# Barebone-packages
This is my barebone python package.
As it is a public template, all you have to do is do click in use this template and set the configs for your new project.


It can be installed with `pip install .` or `pip install -e .`.

Tests can be done with `python3 setup.py test`
And code formatting checking with `python3 setup.py flake8`

Versions should be checked at \_\_init__.py

Dists are generated with:
`python3 setup.py sdist`
`python3 setup.py bdist_wheel`

Uploading to test-pypi can be done with:
`twine upload --repository-url https://test.pypi.org/legacy/ dist/*`