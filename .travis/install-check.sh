#!/usr/bin/env bash

tox -e build && ./test/test_pipipxx.sh "$(pwd)/dist"
