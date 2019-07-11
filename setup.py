#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

setup(
    name="macapype",
    version='0.0.6',
    packages=find_packages(),
    author="David Meunier",
    description="Pipeline for anatomic processing for macaque",
    lisence='BSD 3',
    install_requires=["nipype"]
)