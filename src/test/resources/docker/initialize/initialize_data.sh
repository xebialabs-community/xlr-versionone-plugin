#!/bin/sh
BASEDIR=$(dirname $0)

apk update
apk add curl

####################### XLR server data

    curl -u admin:admin \
        -H "Accept: application/json" \
        -H "Content-type: application/json" \
        -X POST \
        -d @$BASEDIR/data/server-configs.json \
    http://localhost:5516/repository/cis

    curl -u admin:admin \
        -H "Accept: application/json" \
        -H "Content-type: application/json" \
        -X POST \
        -d @$BASEDIR/data/VersionOneTickets.json \
    http://localhost:5516/api/v1/templates/import

exit 0
