#!/bin/bash

if [ -z "$1" ]
  then
    echo "No indicaste el número de plantillas a crear \n el uso es :  ./create-classes.sh <numero> "
    exit 1
fi

for i in $(eval echo {1..$1})
do
    mkdir -p $i
    cp Plantilla-de-clase.md ./$i/.
done