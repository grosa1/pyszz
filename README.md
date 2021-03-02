# PySZZ
This is an open-source implementation of several versions of the SZZ algorithm for detecting bug-inducing commits.

## Requirements
To run PySZZ you need:

- Python 3
- srcML (https://www.srcml.org/) (i.e., the `srcml` command should be in the system path)
- git >= 2.23

## Setup
Run the following command to install the required python dependencies:
```
pip3 install --no-cache-dir -r requirements.txt
```

## Run
To run the tool, simply execute the following command:

```
python3 main.py /path/to/bug-fixes.json /path/to/configuration-file.yml /path/to/repo-directory
```
where:

- `bug-fixes.json` contains a list of information about bug-fixing commits and (optionally) issues. 
This is an example json that can be used with pyszz:
```
[
  {
    "repo_name": "amirmikhak/3D-GIF",
    "fix_commit_hash": "645496dd3c5c89faee9dab9f44eb2dab1dffa3b9"
    "best_scenario_issue_date": "2015-04-23T07:41:52"
  },
  ...
]
```

alternatively:

```
[
  {
    "repo_name": "amirmikhak/3D-GIF",
    "fix_commit_hash":   "645496dd3c5c89faee9dab9f44eb2dab1dffa3b9",
    "earliest_issue_date": "2015-04-23T07:41:52"
  },
  ...
]
```

without issue date:

```
[
  {
    "fix_commit_hash": "30ae3f5421bcda1bc4ef2f1b18db6a131dcbbfd3",
    "repo_name": "grosa1/szztest_mod_change"
  },
  ...
]
```

- `configuration-file.yml` is one of the following, depending on the SZZ variant you want to run:
    - `conf/agszz.yaml`: runs AG-ZZ
    - `conf/lszz.yaml`: runs L-ZZ
    - `conf/rszz.yaml`: runs R-ZZ
    - `conf/maszz.yaml`: runs MA-ZZ
    - `conf/raszz.yaml`: runs RA-ZZ

- `repo-directory` is a folder which contains all the repositories that are required by `bug-fixes.json`. This parameter is not mandatory. In the case of the `repo-directory` is not specified, pyszz will download each repo required by each bug-fix commit in a temporary folder. In the other case, pyszz searches for each required repository in the `repo-directory` folder. The directory structure must be the following:

``` bash
    .
    |-- repo-directory
    |   |-- repouser
    |       |-- reponame 
    .
```

To have different run configurations, just create or edit the configuration files. The available parameters are described in each yml file. In order to use the issue date filter, you have to enable the parameter provided in each configuration file.

_n.b. the difference between `best_scenario_issue_date` and `earliest_issue_date` is described in our [paper](https://arxiv.org/abs/2102.03300). Simply, you can use `earliest_issue_date` if you have the date of the issue linked to the bug-fix commit._

## Quick start
The `test` directory contains some usage examples of pyszz and test cases.
- `start_example1.sh`, `start_example2.sh` and `start_example3.sh` are example usages of pyszz;
- `start_test_lszz.sh` and `start_test_rszz.sh` are test cases for L-SZZ and R-SZZ; 
- `repos_test.zip` and `repos_test_with_issues.zip` contain some downloaded repositories to be used with `bugfix_commits_test.json` and `bugfix_commits_with_issues_test.json` , which are two examples of input json containing bug-fixing commits;
- `comment_parser` contains some test cases for the custom comment parser implemented in pyszz.
