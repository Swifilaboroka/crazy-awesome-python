import github
from library.log import get_logger
from typing import List

logger = get_logger(__name__)


class GithubWrapper:
    def __init__(self, token):
        self.gh = github.Github(token)

    def get_repo(self, name) -> github.Repository:
        logger.debug(f"get_repo: {name}")
        return self.gh.get_repo(name)

    def get_org_repos(self, name) -> List[github.Repository.Repository]:
        logger.debug(f"get_org_repos: {name}")
        org = self.gh.get_organization(name)
        repos = []
        for repo in org.get_repos():
            repos.append(repo)
        return repos

    def get_organization(self, name) -> github.Organization.Organization:
        logger.debug(f"get_organization: {name}")
        return self.gh.get_organization(name)

    def search_github(self, keywords):
        query = "+".join(keywords) + "+in:readme+in:description"
        result = self.gh.search_repositories(query, "stars", "desc")

        print(f"Found {result.totalCount} repo(s)")
        for repo in result:
            print(repo.clone_url)
