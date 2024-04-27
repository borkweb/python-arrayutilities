from setuptools import find_packages, setup

setup(
    name='arrayutilities',
    packages=find_packages(),
    version='1.0.1',
    description='A library for list, dict, and UserDict manipulations.',
    author='Matthew Batchelder',
    author_email='borkweb@gmail.com',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
