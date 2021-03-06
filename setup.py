import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tqc',
    version='0.2.1',
    entry_points = {
        'console_scripts': ['tqc=tqc.cli:main']
    },
    author="Wouter Diesveld",
    author_email="wouter@querytechnology.com",
    description="Command line interface for the TinyQueries Compiler",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/querytechnology/tqc-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
