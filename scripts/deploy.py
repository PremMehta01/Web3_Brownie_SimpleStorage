from brownie import accounts, config, SimpleStorage, network
import os


def deploy_simple_storage():
    # account = accounts[0]  # returns 0 index address from local ganachi-cli, fetch public key
    # account = accounts.load("freecodecamp-demo-account")  # added 'freecodecamp-demo-account' as id(abbreviation/nick name) for private key from metamask, manually via terminal. It load public key
    # account = accounts.add(os.getenv("PRIVATE_KEY"))  # fetching public address based on private key stored in .env file
    # account = accounts.add(config["wallets"]["from_key"])  # check brownie-config file, loads public key

    account = get_account()

    # deploy contract: contract(SimpleStorage) are getting imported, see import above
    simple_storage = SimpleStorage.deploy({"from": account})

    stored_fav_number = simple_storage.retrieve()
    print("Initial favorite_number value: " + str(stored_fav_number))

    txn = simple_storage.store(15, {"from": account})
    txn.wait(1)

    updated_fav_number = simple_storage.retrieve()
    print("Updated favorite_number: " + str(updated_fav_number))


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
