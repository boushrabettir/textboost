from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="textboost",
    version="0.1.1",
    author="Boushra Bettir",
    author_email="boushra.bettir04@csu.fullerton.edu",
    description="A tool leveraged by ML to aid the reading experience through bionic reading.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/boushrabettir/textboost",
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        "nltk>=3.8.1",
        "numpy>=1.23.5",
        "scikit_learn>=1.2.2",
        "textual>=0.30.0",
        "transformers>=4.31.0",
        "tensorflow>=2.13.0",
    ],
    entry_points={"console_scripts": ["textboost=textboost.textboost.main:main"]},
)
