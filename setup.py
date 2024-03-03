from setuptools import setup, find_packages

setup(
    name='ksh_wg_mariadb_adapter',
    version='0.1.0',
    author='Diego Steiner',
    author_email='diego.steiner@openscript.ch',
    packages=find_packages(),
    description='A simple DB adapter for MySQL.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zlict/ksh-wg-mariadb-adapter',
    install_requires=[
        'mysql-connector-python>=8.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
