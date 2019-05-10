"""pipipxx."""
import io
import os
import re

from setuptools import find_packages, setup

VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")
HERE = os.path.abspath(os.path.dirname(__file__))


def read(*args):
    """Read complete file contents."""
    return io.open(os.path.join(HERE, *args), encoding="utf-8").read()


def get_version():
    """Read the version from this module."""
    init = read("src", "pipipxx", "__init__.py")
    return VERSION_RE.search(init).group(1)


def get_requireemnts():
    """Read the requirements file."""
    raw_requirements = read("requirements.txt")
    requirements = []
    dependencies = []

    for req in raw_requirements.splitlines():
        req = req.strip()
        if not req:
            continue
        elif req.startswith("#"):
            continue
        elif "+" in req:
            dependencies.append(req)
        else:
            requirements.append(req)

    return requirements, dependencies


install_requires, dependency_links = get_requireemnts()

setup(
    name="pipipxx",
    version=get_version(),
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/mattsb42/pipipxx",
    author="Matt Bullock",
    author_email="m@ttsb42.com",
    maintainer="Matt Bullock",
    description="pipipxx (pronounced pipx in pipx): Bootstrap your pipx with pipx.",
    long_description=read("README.rst"),
    keywords="pipipxx pipipxx",
    data_files=["README.rst", "CHANGELOG.rst", "LICENSE", "requirements.txt"],
    licence="Apache 2.0",
    install_requires=install_requires,
    dependency_links=dependency_links,
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
