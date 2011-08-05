from setuptools import setup
import os

def read(*rnames):
        return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name='peeper',
    version='0.1.0',
    author='Matt Luongo',
    author_email='mhluongo@gmail.com',
    description='A simple Javascript expression builder written for Python.',
    url = "http://packages.python.org/jexp",
    packages=['jexp',],
    include_package_data=True,
    zip_safe=False,
    long_description=read('README.rst'),
    platforms=['posix'],
    tests_require=read('test_requirements.txt').split('\n'),
    install_requires=read('requirements.txt').split('\n'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python'
    ]
)