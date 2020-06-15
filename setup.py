import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyBSDate',
    version='0.3.0rc',
    packages=['pyBSDate'],
    url='https://github.com/SushilShrestha/pyBSDate',
    download_url='https://github.com/SushilShrestha/pyBSDate/tarball/0.3.0rc',
    license='MIT',
    author='sushil',
    author_email='afahocci@gmail.com',
    package_data={},
    description='Python BS date conversion utility',
    long_description=long_description,
    long_description_content_type="text/markdown",
)
