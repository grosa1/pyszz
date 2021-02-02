import logging as log
from typing import List, Set

from git import Commit
from pydriller.metrics.process.lines_count import LinesCount
from szz.core.abstract_szz import ImpactedFile
from szz.ma_szz import MASZZ


class LSZZ(MASZZ):
    """
    Large-SZZ implementation.
    """

    def __init__(self, repo_full_name: str, repo_url: str, repos_dir: str = None):
        super().__init__(repo_full_name, repo_url, repos_dir)

    # TODO: add parse and type check on kwargs
    def find_bic(self, fix_commit_hash: str, impacted_files: List['ImpactedFile'], **kwargs) -> Set[Commit]:
        """
        Find bug introducing commits candidates.

        :param str fix_commit_hash: hash of fix commit to scan for buggy commits
        :param List[ImpactedFile] impacted_files: list of impacted files in fix commit
        :key ignore_revs_file_path (str): specify ignore revs file for git blame to ignore specific commits.
        :key mod_files_treshold (int): if the number of modified files exceeds the threshold, the commit will be
            excluded (default 20)
        :key detect_move_from_other_files (DetectLineMoved): detect lines moved or copied from other files that were
            modified in the same commit, from parent commits or from any commit (default DetectLineMoved.SAME_COMMIT)
        :key metric (MetricType): define which metric to use for commit selection (default MetricType.LINES_COUNT)
        :returns Set[Commit] a set of bug introducing commits candidates, represented by Commit object
        """

        bic_candidates = super().find_bic(fix_commit_hash=fix_commit_hash, impacted_files=impacted_files, **kwargs)

        bic_candidate = None
        max_mod_lines = 0
        for commit in bic_candidates:
            lc = LinesCount(path_to_repo=self.repository_path, from_commit=commit.hexsha, to_commit=commit.hexsha).count()
            mod_lines_count = 0
            for k in lc.keys():
                mod_lines_count += lc.get(k)

            if mod_lines_count > max_mod_lines:
                max_mod_lines = mod_lines_count
                bic_candidate = commit

        log.info(f"Selected bug introducing commit: {bic_candidate}")

        return {bic_candidate}
