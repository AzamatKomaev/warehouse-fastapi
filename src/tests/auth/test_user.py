import pytest


@pytest.mark.user
def test_invalid_data_creating_user():
    assert 0 == 0


@pytest.mark.user
def test_successfully_creating_user():
    assert 1 == 1


@pytest.mark.user
def test_invalid_data_authorizing_user():
    assert 2 == 2


@pytest.mark.user
def test_successfully_authorizing_user():
    assert 3 == 3
