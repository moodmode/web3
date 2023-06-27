import requests
from web3 import Web3

from config import RPC


def get_accound_addres(private_key):
    network = 'BSC'
    web3 = Web3(Web3.HTTPProvider(RPC[network]))
    account = web3.eth.account.from_key(private_key)
    my_address = account.address
    return my_address

def intToDecimal(qty, decimal):
    return int(qty * int("".join(["1"] + ["0"]*decimal)))

def decimalToInt(qty, decimal):
    return qty/ int("".join((["1"]+ ["0"]*decimal)))


def get_api_call_data(url):


    call_data = requests.get(url)

    # cprint(f'call_data.status_code : {call_data.status_code}', 'blue')
    print(call_data)
    if call_data.status_code == 200:
        api_data = call_data.json()
        return api_data
    else:
        return False

