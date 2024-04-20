### Run Unittests
```
python -m unittest discover
```


### publish to pypi
```
setup.py sdist
pip install twine
# update ~/.pypirc with username and password
twine upload -r pyBSDate dist/*
```

- https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/
- https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives
