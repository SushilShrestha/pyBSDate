import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyBSDate',
    version='0.3.2',
    packages=['pyBSDate'],
    url='https://github.com/SushilShrestha/pyBSDate',
    download_url='https://github.com/SushilShrestha/pyBSDate/tarball/0.3.2',
    license='MIT',
    author='sushil',
    author_email='afahocci@gmail.com',
    package_data={},
    description='Python BS date conversion utility',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ]
)
