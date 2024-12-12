#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <number>"
  exit 1
fi

if ! [[ "$1" =~ ^[0-9][0-9]$ ]]; then
  echo "Error: wrong argument"
  exit 1
fi

touch "solutions/day${1}.py"
touch "day${1}example.txt"
touch "day${1}input.txt"
