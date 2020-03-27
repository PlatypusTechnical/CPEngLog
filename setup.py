from setuptools import setup

setup(
    name='CPEngLog',
    version='0.1dev',
    author='Lee Walsh',
    packages=['cpenglog',],
    scripts=['bin/runlog.py'],
    license='LICENSE',
    description='CPD reporting for CPEng',
    long_description=open('README.md').read(),
    install_requires=[
        'pandas >= 0.25.3',
        'xlrd >= 1.2.0',
    ],
)