from setuptools import find_packages, setup

setup(
    name='coc_bot',
    version='1.0',
    description='Library to manage Discord bot commands.',
    license='',
    author='Gabriel Michel',
    author_email='jose.michel@wizeline.com',
    package_dir={'': 'lib'},
    packages=find_packages(where='lib'),
    install_requires=[
        'boto3',
        'discord.py',
        'coc.py'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Copyright 2021, Wizeline. All rights reserved.',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)