#! /bin/bash
before_install:
    export NG_CLI_ANALYTICS=ci

script:
    cd backend/static
    flask run --host 0.0.0.0 &
    cd ../..
    ng serve --host 0.0.0.0
