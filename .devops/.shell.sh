#!/bin/bash
set -e
if [ -z "$1" ]
  then
    echo "No app name provided"
    exit 1
fi
APP_NAME=$1

if [ -z "$2" ]
  then
    echo "No namespace provided"
    exit 1
fi
NAMESPACE=$2

if [ -z "$3" ]
  then
    echo "No container provided"
    exit 1
fi
CONTAINER=$3

kubectl -n $NAMESPACE exec -it $(kubectl -n $NAMESPACE get po -l "name=$APP_NAME" -o jsonpath='{.items[0].metadata.name}') -c $CONTAINER -- python manage.py shell