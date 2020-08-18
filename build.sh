#!/usr/bin/env bash

export $(cat config/.env | grep "^[^#;]")
docker build \
        --build-arg GIT_CONFIG_USER_NAME=$GIT_CONFIG_USER_NAME  \
        --build-arg GIT_CONFIG_EMAIL=$GIT_CONFIG_EMAIL \
        -t dvc-2-iris-demo:latest .
