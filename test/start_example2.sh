#!/bin/bash

# preparing local repo-directory
unzip repos_test_with_issues.zip

# executing R-SZZ switching back to main pyszz direcory
# in this case, the bug-fixes.json contains bugfix commits considering issue date (enabled in R-SZZ config file)
cd .. && python3 main.py test/bugfix_commits_with_issues_test.json conf/rszz.yml test/repos_test_with_issues/