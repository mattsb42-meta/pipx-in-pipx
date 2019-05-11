"""pipipxx."""
import io
import os
import sys

from setuptools import setup
from setuptools.command.install import install

HERE = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(HERE, "src"))

import pipipxx  # noqa isort:skip pylint: disable=wrong-import-position


if sys.version_info < (3, 6, 0):
    exit("Python 3.6+ is required")


class BootstrapInstall(install):
    """Bootstrap "install" command that runs the pipx bootstrap."""

    def run(self):
        """Bootstrap pipx."""
        pipipxx.bootstrap()


def read(*args):
    """Read complete file contents."""
    return io.open(os.path.join(HERE, *args), encoding="utf-8").read()


setup(
    name="pipipxx",
    version=pipipxx.__version__,
    packages=[],
    package_dir={"": "src"},
    url="https://github.com/mattsb42/pipipxx",
    author="Matt Bullock",
    author_email="m@ttsb42.com",
    maintainer="Matt Bullock",
    description="pipipxx (pronounced pipx in pipx): Bootstrap your pipx with pipx.",
    long_description=read("README.rst"),
    keywords="pipipxx pipx",
    data_files=["README.rst", "CHANGELOG.rst", "LICENSE", "requirements.txt"],
    license="Apache 2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    cmdclass=dict(install=BootstrapInstall),
)
