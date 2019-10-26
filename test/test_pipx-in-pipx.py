"""
Try to "install" pipx-in-pipx via shell commands.
"""
import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path


def _fail(error_message: str):
    sys.exit(f"ERROR: {error_message}")


def _banner(message: str):
    print(f" {message} ".center(64))


def _target_source_build(dist_path: str) -> Path:
    _banner("Locating the source build")

    try:
        dist_dir = Path(dist_path)
        if not dist_dir.is_dir():
            # Normalize so that this error is raised
            #  whether the path does not exist
            #  or of it is not a directory.
            raise FileNotFoundError
    except FileNotFoundError:
        _fail("dist-directory does not exist!")

    source_builds = [i for i in dist_dir.iterdir() if i.is_file() and i.suffixes[-2:] == [".tar", ".gz"]]
    if not source_builds:
        _fail(f"dist-directory {dist_dir.name} contains no source build artifacts!")

    return source_builds[-1]


def _verify_is_installed(fake_home: Path) -> Path:
    _banner("Verifying the pipx IS installed")
    try:
        pipx_venv = fake_home / ".local" / "pipx" / "venvs" / "pipx"
        pipx_bin = fake_home / ".local" / "Scripts" if os.name == "nt" else "bin" / "pipx"
        if not (pipx_venv.is_dir() and pipx_bin.is_file()):
            # Normalize so that this error is raised
            #  whether the path does not exist
            #  or of it is not a directory.
            raise FileNotFoundError
        return pipx_bin
    except FileNotFoundError:
        _fail(f"pipx is not installed in {fake_home.name}")


def _verify_not_installed(fake_home: Path):
    _banner("Verifying the pipx is NOT installed")
    try:
        _verify_is_installed(fake_home)
    except SystemExit:
        # We *want* this to fail!
        pass


def install_and_verify(source_build: Path, fake_home: Path) -> None:
    _verify_not_installed(fake_home)

    env = os.environ.copy()
    env["HOME"] = fake_home.name
    subprocess.run(["pip", "install", source_build.name, "-vv"], check=True)

    pipx_bin = _verify_is_installed(fake_home)

    result = subprocess.run([pipx_bin.name, "--help"], check=False)
    print(result.stdout)
    print(result.stderr)


def main(args=None):
    parser = argparse.ArgumentParser(description="pipx-in-pipx tester")
    parser.add_argument("--dist-directory", required=True)

    parsed_args = parser.parse_args(args)

    source_build = _target_source_build(parsed_args.dist_directory)

    with tempfile.TemporaryDirectory() as fake_home:
        install_and_verify(source_build, Path(fake_home))


if __name__ == "__main__":
    main()
