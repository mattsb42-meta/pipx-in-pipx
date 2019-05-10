"""pipipxx."""
import io
import os
import re
import sys

from setuptools import setup

if sys.version_info < (3, 6, 0):
    print("Python 3.6+ is required")
    exit(1)

VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")
HERE = os.path.abspath(os.path.dirname(__file__))


def read(*args):
    """Read complete file contents."""
    return io.open(os.path.join(HERE, *args), encoding="utf-8").read()


def get_version():
    """Read the version from this module."""
    init = read("src", "pipipxx", "__init__.py")
    return VERSION_RE.search(init).group(1)


setup(
    name="pipipxx",
    version=get_version(),
    url="https://github.com/mattsb42/pipipxx",
    author="Matt Bullock",
    author_email="m@ttsb42.com",
    maintainer="Matt Bullock",
    description="pipipxx (pronounced pipx in pipx): Bootstrap your pipx with pipx.",
    long_description=read("README.rst"),
    keywords="pipipxx pipipxx",
    data_files=["README.rst", "CHANGELOG.rst", "LICENSE", "requirements.txt"],
    licence="Apache 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython"
    ]
)
