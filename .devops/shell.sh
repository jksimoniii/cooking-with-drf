#!/bin/bash
NAMESPACE=${1:-dev}
CONTAINER=${2:-app}
echo "Connecting to myproj.$NAMESPACE.$CONTAINER..."
./.devops/.shell.sh myproj $NAMESPACE $CONTAINER