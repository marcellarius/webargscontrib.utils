from setuptools import setup

setup(
    name="webargscontrib.utils",
    version="0.1",
    description="A collection of utility functions for webargs",
    author="Sam Douglas",
    author_email="sam.douglas32@gmail.com",
    packages=["webargscontrib.utils"],
    namespace_packages=["webargscontrib"],
    install_requires=['webargs'])