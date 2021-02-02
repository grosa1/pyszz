# PySZZ
This is an open-source implementation of several versions of the SZZ algorithm for detecting bug-inducing commits.

## Requirements
To run PySZZ you need:

- Python 3
- srcML (https://www.srcml.org/) (i.e., the `srcml` command should be in the path)
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

- `bug-fixes.json` contains a list of information about bug-fixing commits and (optionally) issues
- `configuration-file.yml` is one of the following, depending on the SZZ variant you want to run:
    - `conf/agszz.yaml`: runs AG-ZZ
    - `conf/lszz.yaml`: runs L-ZZ
    - `conf/rszz.yaml`: runs R-ZZ
    - `conf/maszz.yaml`: runs MA-ZZ
    - `conf/raszz.yaml`: runs RA-ZZ
- `repo-directory` is a folder which contains all the repositories that are required by `bug-fixes.json`

To have different run configurations, just create or edit the configuration files. The available parameters are described in each yml file.

## Input data
The `data` dir contains two sub-folders:
- `data/langs_only` contains the json files extracted from the dataset filtered only by the defined langs for the experiment.
- `data/with_whitelist` contains the json files extracted from the dataset filtered by the file extensions defined in the [whitelist csv](https://gitlab.reveal.si.usi.ch/gbavota/icse2021-szz-oracle/-/blob/master/database/langs.csv).

The input json files are the following:
- `bugfix_commits_no_issues.json`: contains only fix commits having no issue references.
- `bugfix_commits_issues_only.json`: contains only fix commits that reference one or more issues, where the `earliest_issue_date` field is the earliest creation date among the referenced issues;
- `bugfix_commits_all.json`: contains all the fix commits, where if there are no referenced issues, the field `best_scenario_issue_date` will be the earliest creation date among the linked bug commits with a time offset of 60 seconds. Otherwise, the field `earliest_issue_date` will be the earliest issue creation date;
