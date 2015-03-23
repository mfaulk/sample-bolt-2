#!/bin/bash

# Fill this in
APP_NAME="sample-bolt-2"

# Fill this in
GIT_REPO="github.com/mfaulk/sample-bolt-2"

sed -e "s:APP_NAME:${APP_NAME}:g" \
	-e "s:GIT_REPO:${GIT_REPO}:g" \
	kafka-bolt.service.template > ${APP_NAME}.service