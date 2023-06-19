

from setuptools import setup , find_packages

setup(
    name= 'src',
    version= '0.0.1',
    author= 'vilas',
    author_email= 'tadevilas@gmail.com',
    install_requires =['pandas', 'numpy', 'flask'],
    packages= find_packages()
)