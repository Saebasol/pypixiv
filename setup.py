import setuptools  # type: ignore
from setuptools import setup  # type: ignore

import pypixiv

setup(
    name="pypixiv",
    author="Ryu JuHeon",
    author_email="SaidBySolo@gmail.com",
    url="https://github.com/Saebasol/pypixiv",
    version=pypixiv.__version__,
    long_description=open("README.md", "rt", encoding="UTF8").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),  # type: ignore
    description="Pixiv ajax wrapper",
    python_requires=">=3.9",
)
