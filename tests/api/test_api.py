import pytest


@pytest.mark.change
def test_remove_first_name(user):
    user.remove()
    assert user.first_name == ''


@pytest.mark.check
def test_first_name(user):
    assert user.first_name == 'Henry'


@pytest.mark.check
def test_last_name(user):
    assert user.last_name == 'Chinaski'
