#!/usr/bin/env bash

tox -e build && ./test/integration/test_pipipxx.sh "$(pwd)/dist"
