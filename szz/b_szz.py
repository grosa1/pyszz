import logging as log
import traceback
from typing import List, Set

from git import Commit

from szz.core.abstract_szz import AbstractSZZ, ImpactedFile


class BaseSZZ(AbstractSZZ):
    """
    Base SZZ implementation.

    Supported **kwargs:

    * ignore_revs_file_path

    """

    def __init__(self, repo_full_name: str, repo_url: str, repos_dir: str = None):
        super().__init__(repo_full_name, repo_url, repos_dir)

    def find_bic(self, fix_commit_hash: str, impacted_files: List['ImpactedFile'], **kwargs) -> Set[Commit]:
        """
        Find bug introducing commits candidates.

        :param str fix_commit_hash: hash of fix commit to scan for buggy commits
        :param List[ImpactedFile] impacted_files: list of impacted files in fix commit
        :key ignore_revs_file_path (str): specify ignore revs file for git blame to ignore specific commits.
        :returns Set[Commit] a set of bug introducing commits candidates, represented by Commit object
        """

        log.info(f"find_bic() kwargs: {kwargs}")

        ignore_revs_file_path = kwargs.get('ignore_revs_file_path', None)
        self._set_working_tree_to_commit(fix_commit_hash)

        bug_introd_commits = set()
        for imp_file in impacted_files:
            try:
                blame_data = self._blame(
                    rev='HEAD^',
                    file_path=imp_file.file_path,
                    modified_lines=imp_file.modified_lines,
                    ignore_revs_file_path=ignore_revs_file_path,
                    ignore_whitespaces=False,
                    skip_comments=False
                )
                bug_introd_commits.update([entry.commit for entry in blame_data])
            except:
                print(traceback.format_exc())

        if 'issue_date_filter' in kwargs and kwargs['issue_date_filter']:
            before = len(bug_introd_commits)
            bug_introd_commits = [c for c in bug_introd_commits if c.committed_date <= kwargs['issue_date']]
            log.info(f'Filtering by issue date returned {len(bug_introd_commits)} out of {before}')
        else:
            log.info("Not filtering by issue date.")
        
        return bug_introd_commits
