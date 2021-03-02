#!/bin/bash

# preparing local test repo-directory
unzip repos_test.zip

# executing L-SZZ test
cd .. && \
    cp test/test_lszz_main.py . && \
    python3 test_lszz_main.py test/bugfix_commits_test.json conf/lszz.yml test/repos_test/ && \
    rm test_lszz_main.py
