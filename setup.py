#!/usr/bin/env python
import sys
from setuptools import setup


def get_install_requires():
    res = ['elasticsearch>=5.4.0,<7.0.0']
    res.append('apscheduler>=3.5.0')
    return res


try:
    from cx_Freeze import setup, Executable

    try:
        import certifi

        cert_file = certifi.where()
    except ImportError:
        cert_file = ''

    base = None
    if sys.platform == "win32":
        base = "Win32GUI"

    esops_exe =  Executable(
        "esops/main.py",
        base=base,
        targetName = "esops",
    )

    buildOptions = dict(
        packages=[],
        excludes=[],
        include_files=[cert_file],

    )

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
        options={"build_exe": buildOptions},
        executables=[esops_exe],
    )

except ImportError:
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
        ]}
    )
