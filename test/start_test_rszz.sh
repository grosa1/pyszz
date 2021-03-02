#!/bin/bash

# preparing local test repo-directory
unzip repos_test.zip

# executing R-SZZ test
cd .. && \
    cp test/test_rszz_main.py . && \
    python3 test_rszz_main.py test/bugfix_commits_test.json conf/rszz.yml test/repos_test/ && \
    rm test_rszz_main.py