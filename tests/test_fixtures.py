import pytest


@pytest.mark.check
def test_change_first_name(user):
    assert user.first_name == 'Henry'


@pytest.mark.check
def test_change_last_name(user):
    assert user.last_name == 'Chinaski'
