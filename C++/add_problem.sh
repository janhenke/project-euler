#!/bin/sh

if [ "$#" -ne 1 ] || [ -z "$1" ]; then
  echo "Usage: $0 PROBLEM_NUMBER" >&2
  exit 1
fi

PROBLEM_NUMBER=$1
BASE_DIR=$( dirname -- "$( readlink -f -- "$0"; )"; )

cp -r "$BASE_DIR"/template "$BASE_DIR"/"p$PROBLEM_NUMBER"
sed -i '' "s/###/$PROBLEM_NUMBER/" "$BASE_DIR"/"p$PROBLEM_NUMBER"/CMakeLists.txt "$BASE_DIR"/"p$PROBLEM_NUMBER"/main.cpp

echo "add_subdirectory(p$PROBLEM_NUMBER)" >> "$BASE_DIR"/CMakeLists.txt
