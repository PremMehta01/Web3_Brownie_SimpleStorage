from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[
        -1
    ]  # -1 to get the lastest contract, you can put 0 to get the first contract
    print(simple_storage.retrieve())


def main():
    read_contract()
