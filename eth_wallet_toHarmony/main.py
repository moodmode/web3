from pyhmy import util

# Read Ethereum addresses from a separate file
with open('ethereum_addresses.txt', 'r') as file:
    ethereum_addresses = file.read().splitlines()

one_addresses = []

# Convert Ethereum addresses to Harmony addresses
for ethereum_address in ethereum_addresses:
    one_address = util.convert_hex_to_one(ethereum_address)
    one_addresses.append(one_address)

with open("Harmony_wallets.txt", "w") as file:
    for one_address in one_addresses:
        print(one_address)
        file.write(one_address + "\n")