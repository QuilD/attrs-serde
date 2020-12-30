from setuptools import setup

setup(
    name='attrs-serde',
    version='0.3.1',
    description='A serialization addon for attrs',
    url='https://github.com/QuilD/attrs-serde',
    keywords=['attrs', 'serialization', 'dict', 'data', 'nested', 'functional'],
    author='Dotan Nahum',
    author_email='jondotan@gmail.com',
    license='MIT',
    install_requires=[
        'toolz~=0.11.0', 'cytoolz~=0.11.0', 'attrs~=20.0'
    ],
)