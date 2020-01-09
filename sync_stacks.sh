#!/bin/sh
set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

rsync -vrlt --delete stacks root@managers.sys.hacktrinity.org:/mnt/docker-shared/
