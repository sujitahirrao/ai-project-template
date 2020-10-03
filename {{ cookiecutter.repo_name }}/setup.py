import os
from setuptools import find_packages, setup


# Utility function to read the README file.
# Used for the long_description.
def read(file_name):
    return open(os.path.join(os.path.dirname(__file__),
                             file_name)).read()


setup(
    name="{{ cookiecutter.package_name }}",
    packages=find_packages(exclude=["tests", "*visualization"]),
    version="0.1.0",
    description="{{ cookiecutter.description }}",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    long_description=read("README.md"),
)
