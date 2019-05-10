"""pipipxx."""
import io
import os
import re
import sys

from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(HERE, "src"))

import pipipxx  # noqa isort:skip


if sys.version_info < (3, 6, 0):
    exit("Python 3.6+ is required")

VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")


def read(*args):
    """Read complete file contents."""
    return io.open(os.path.join(HERE, *args), encoding="utf-8").read()


setup(
    name="pipipxx",
    version=pipipxx.__version__,
    packages=[""],
    package_dir={"": "src"},
    url="https://github.com/mattsb42/pipipxx",
    author="Matt Bullock",
    author_email="m@ttsb42.com",
    maintainer="Matt Bullock",
    description="pipipxx (pronounced pipx in pipx): Bootstrap your pipx with pipx.",
    long_description=read("README.rst"),
    keywords="pipipxx pipx",
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
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)
