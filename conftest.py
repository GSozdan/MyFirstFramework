import pytest
from modules.api.clients.github import GitHub


class User:

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def create(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def remove(self):
        self.first_name = ''
        self.last_name = ''


@pytest.fixture
def user():
    user = User()
    user.create('Henry', 'Chinaski')
    yield user
    user.remove()


@pytest.fixture
def github_api():
    return GitHub()
