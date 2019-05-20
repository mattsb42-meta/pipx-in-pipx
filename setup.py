"""Bootstrap pipx without installing anything to any system Python environments."""
import io
import os
import pathlib
import subprocess  # nosec : bandit B404 is addressed by only executing pre-defined commands
import sys
import tempfile
import venv

from setuptools import setup
from setuptools.command.install import install

if sys.version_info < (3, 6, 0):
    # pipx requires Python 3.6+ https://github.com/pipxproject/pipx/pull/39
    # Fail early.
    exit("Python 3.6+ is required")


__version__ = "0.0.1b0"
HERE = os.path.abspath(os.path.dirname(__file__))
UPDATE_PIP = "python -m pip install --upgrade pip"
INSTALL_BOOTSTRAP_REQUIREMENTS = "python -m pip install pipx userpath"
BOOTSTRAP_PIPX = f"python -m pipx install pipx --python {sys.executable} --force"
LOCAL_BIN = pathlib.Path.home() / ".local" / "bin"
PATCH_PATH = f"python -m userpath append {LOCAL_BIN}"
VERIFY_PATH = f"python -m userpath verify {LOCAL_BIN}"
NOTICE_WIDTH = 64


def _build_venv(venv_dir: str):
    venv.create(venv_dir, clear=True, with_pip=True)
    _execute_in_venv(venv_dir, UPDATE_PIP)
    _execute_in_venv(venv_dir, INSTALL_BOOTSTRAP_REQUIREMENTS)


def _execute_command(command: str) -> (str, str):
    proc = subprocess.run(  # nosec : bandit B602 is addressed by only executing pre-defined commands
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8", shell=True
    )
    print(proc.stdout, flush=True)  # noqa
    if proc.stderr:
        print(proc.stderr, file=sys.stderr, flush=True)  # noqa
    return proc.stdout, proc.stderr


def _execute_in_venv(venv_dir: str, command: str) -> (str, str):
    return _execute_command(os.path.join(venv_dir, "bin", command))


def bootstrap():
    """Bootstrap ``pipx`` in your ``~/.local/`` using ``pipx`` in a temporary venv."""
    if "VIRTUAL_ENV" in os.environ:
        raise EnvironmentError("pipipxx cannot be used inside a virtual environment.")

    with tempfile.TemporaryDirectory() as venv_dir:
        # 1. Create tempfiles venv.
        # 2. Install pipx in tempfiles venv.
        print(" Building bootstrapping venv ".center(NOTICE_WIDTH, "#"), flush=True)  # noqa
        _build_venv(venv_dir)
        # 3. Use tempfiles pipx to install pipx pipx.
        print(" Installing local pipx using bootstrapping pipx ".center(NOTICE_WIDTH, "#"), flush=True)  # noqa
        _execute_in_venv(venv_dir, BOOTSTRAP_PIPX)
        # 4. Append ~/.local/bin to path.
        print(" Verifying that PATH includes local bin ".center(NOTICE_WIDTH, "#"), flush=True)  # noqa
        _execute_in_venv(venv_dir, PATCH_PATH)
        # 5. Determine if the shell needs to be restarted and print an appropriate message.
        _execute_in_venv(venv_dir, VERIFY_PATH)


class BootstrapInstall(install):
    """Bootstrap "install" command that runs the pipx bootstrap."""

    def run(self):
        """Bootstrap pipx."""
        bootstrap()


def read(*args):
    """Read complete file contents."""
    return io.open(os.path.join(HERE, *args), encoding="utf-8").read()


setup(
    name="pipipxx",
    version=__version__,
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
