#!/usr/bin/env bash

die () {
    echo >&2 "$@"
    exit 1

}

[[ "$#" -eq 1 ]] || die "Must provide dist directory"
DIST_DIR=$1

setup () {

    HOME_CACHE=$HOME

    echo "Creating temp dir for custom home"
    TMP_HOME=`mktemp -d`
    echo "Using temporary home at: ${TMP_HOME}"
    export HOME=${TMP_HOME}

}

cleanup () {

    echo "Cleaning up temp home"
    export HOME=${HOME_CACHE}
    rm -rf ${TMP_HOME}

}

install_and_verify () {

    echo "Locating the source build."
    DIST_FILE=`ls ${DIST_DIR}/pipipxx-*.tar.gz | tail -1`

    echo "Verifying the pipx is NOT installed"
    [[ -d "${TMP_HOME}/.local/pipx/venvs/pipx" ]] && die "ERROR: pipx venv already exists!"
    [[ -h "${TMP_HOME}/.local/bin/pipx" ]] && die "ERROR: pipx bin symlink already exists!"

    echo "pipx installing pipx"
    pip install ${DIST_FILE} -vv

    echo "Verifying the pipx IS installed"
    [[ -d "${TMP_HOME}/.local/pipx/venvs/pipx" ]] || die "ERROR: pipx venv not created!"
    [[ -h "${TMP_HOME}/.local/bin/pipx" ]] || die "ERROR: pipx bin symlink not created!"

    ( ${TMP_HOME}/.local/bin/pipx --help 2>&1 )

}

{
    setup && install_and_verify
}

cleanup
