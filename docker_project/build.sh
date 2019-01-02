#!/bin/bash

NAME=`python -m project.config |tail -n 1`

EXTRA="--add-host mirrors.163.com:59.111.0.251"

docker build ${EXTRA} -t ${NAME} -f build/Dockerfile
