#!/usr/bin/env python
from setuptools import setup
import py2exe

def get_install_requires():
    res = ['elasticsearch>=5.4.0,<7.0.0']
    res.append('apscheduler>=3.5.0')
    return res


setup(
    name="esops",
    version="1.0",
    keywords=("elasticsearch", "ops"),
    description="a tool for elasticsearch ops",
    long_description="a tool for elasticsearch ops",
    license="Apache License, Version 2.0",

    author="wenpos",
    author_email="test@test.com",
    url="https://github.com/wenpos/esops",

    packages=["esops"],
    include_package_data=True,
    install_requires=get_install_requires(),
    entry_points={"console_scripts": [
        "espos = esops.mian:main",
    ]},
    
)
