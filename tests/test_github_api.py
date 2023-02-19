import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('octocat')
    assert user['login'] == 'octocat'


@pytest.mark.api
def test_user_not_exists(github_api):
    user = github_api.get_user("jim-lindsay")
    assert user['message'] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    repo = github_api.search_repo("become-qa-auto")
    assert repo["total_count"] == 31


@pytest.mark.api
def test_user_cannot_be_found(github_api):
    repo = github_api.search_repo("skynet-dtek")
    assert repo["total_count"] == 0
