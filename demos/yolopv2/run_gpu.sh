#!/usr/bin/env -S bash -e
docker build . -t norfair-yolopv2
docker run -it --rm \
        --gpus all \
        --shm-size=1gb \
        -v `realpath .`:/demo \
        norfair-yolopv2 \
        bash
