# Barebone-packages
<p>This is my barebone python package.
<p>As it is a public template, all you have to do is do click in use this template and set the configs for your new project.

## Settings 
<p>After the pythonbare folder name and module.py name are changed, these settings need to be changed as well: 

`setup.py/(package_dir and py_modules).`

<p>package_dir should reflect the new name of the folder and the python modules. Like in the example below.

```python
    package_dir={'':'new_folder_name'},
    py_modules=['new_module_name_without_.py'],
```

> the new_folder_name shouldn't have any __-__ or it won't be imported.


---

## Using the package 

It can be installed with `pip install .` or `pip install -e .`.

After installing, it can be imported using 
`import new_folder_name.new_module_name`

Tests can be done with `python3 setup.py test`
And code formatting checking with `python3 setup.py flake8`

Versions should be checked at \_\_init__.py

Dists are generated with:
`python3 setup.py sdist`
`python3 setup.py bdist_wheel`

Uploading to test-pypi can be done with:
`twine upload --repository-url https://test.pypi.org/legacy/ dist/*`