#!/bin/bash

case "${1}" in
  write)
    npx prettier --config .prettier.toml --write -- '**/*.{md,yaml,yml}'
    ;;
  check)
    npx prettier --config .prettier.toml --check -- '**/*.{md,yaml,yml}'
    ;;
  *)
    echo "mode required!"
    echo "${0} [write/check]"
    exit 1
    ;;
esac
