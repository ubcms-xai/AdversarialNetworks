#!/usr/bin/env bash
docker run --rm -it -v ${PWD}:${PWD} -w ${PWD} -p $1:8888 --entrypoint /bin/bash $2
