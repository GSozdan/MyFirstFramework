import pytest
from modules.api.clients.github import GitHub


class User:
    def __init__(self, first_name=None, last_name=None) -> None:
        self.first_name = first_name
        self.last_name= last_name

    def create(self):
        self.first_name = 'Henry'
        self.last_name = 'Chinaski'

    def remove(self):
        self.first_name = ""
        self.last_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()
    yield user
    user.remove()


@pytest.fixture
def github_api():
    return GitHub()
