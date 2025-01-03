# coding='utf-8'
import codecs, os
from setuptools import setup
long_description = open('README.md').read()

def getVersion():
    firstline = read("myhttps/__init__.py").splitlines()[0]
    ver = firstline.split("'")[1]
    return ver

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()
# print(getVersion())
ver = getVersion()
setup(
    name='myhttps',
    version=ver,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Yang Li',
    author_email='leeyang1991@gmail.com',
    packages=['myhttps'],
    entry_points={
        "console_scripts": [
            "myhttps=myhttps.__main__:main",
        ],
    },
    url='https://github.com/leeyang1991/myhttps',
    python_requires='>=3',
    install_requires=[
    'pyOpenSSL',
    'outdated',
    'urllib3',
    'requests',
    'beautifulsoup4',
    ],
)

