from setuptools import setup, find_packages

setup(
    name='aes_module',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pycryptodome',
    ],
)
