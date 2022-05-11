from brownie import accounts, SimpleStorage


def test_deploy():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # Act
    initial_fav_value = simple_storage.retrieve()
    expected_fav_value = 0

    # Assert
    assert initial_fav_value == expected_fav_value


def test_updating_fav_value():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    # Act
    expected = 15
    simple_storage.store(expected, {"from": account})

    # Assert
    assert expected == simple_storage.retrieve()
