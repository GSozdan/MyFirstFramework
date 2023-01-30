import pytest


@pytest.mark.change
def test_remove_name(user):
    user.remove()
    assert user.name == ''


@pytest.mark.check
def test_name(user):
    assert user.name == 'Henry'


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == "Chinaski"
