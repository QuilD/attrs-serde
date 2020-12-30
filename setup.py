from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='attrs-serde',
    version='0.3.2',
    description='A serialization addon for attrs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/QuilD/attrs-serde',
    keywords=['attrs', 'serialization', 'dict', 'data', 'nested', 'functional'],
    author='Dotan Nahum',
    author_email='jondotan@gmail.com',
    license='MIT',
    install_requires=[
        'toolz~=0.11.0', 'cytoolz~=0.11.0', 'attrs~=20.0'
    ],
    packages=find_packages(),
    python_requires='>=3.6',
)