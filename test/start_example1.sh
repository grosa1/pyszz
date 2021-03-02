#!/bin/bash

# preparing local repo-directory
unzip repos_test.zip

# executing MA-SZZ switching back to main pyszz direcory
# in this case, the bug-fixes.json contains bugfix commits withouth issue date
cd .. && python3 main.py test/bugfix_commits_test.json conf/maszz.yml test/repos_test/