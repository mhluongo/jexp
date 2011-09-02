from setuptools import setup
import os

def read(*rnames):
        return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='jexp',
    version='0.1.2',
    author='Matt Luongo',
    author_email='mhluongo@gmail.com',
    description='A simple Javascript expression builder written for Python.',
    url = "http://packages.python.org/jexp",
    packages=['jexp',],
    include_package_data=True,
    zip_safe=False,
    long_description=read('README.rst'),
    platforms=['posix'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python'
    ]
)
