import datetime
import json
import random

from web3 import Web3

from config import DATA, network_erc20_abi
from helping_commands import decimalToInt, intToDecimal


def stake_stg(private_key, address):
    contract_address = '0xD4888870C8686c748232719051b677791dBDa26D'

    chain = 'bsc'
    rpc = DATA['bsc']['rpc']
    web3 = Web3(Web3.HTTPProvider(rpc))
    ERC20_ABI=''
    if ERC20_ABI == '':
        ERC20_ABI = json.loads('''[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint256","name":"_initialSupply","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"decimals_","type":"uint8"}],"name":"setupDecimals","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]''')
    contract = web3.eth.contract('0xB0D502E938ed5f4df2E681fE6E419ff29631d62b', abi=ERC20_ABI)
    balance_wei = contract.functions.balanceOf(address).call()

    token_decimal = 18

    human_readable = decimalToInt(balance_wei, token_decimal)*0.98
    print(human_readable)
    contr_addr = '0xB0D502E938ed5f4df2E681fE6E419ff29631d62b'
    contr = get_erc20_contract(web3, contr_addr, ERC20_ABI)
    amountall = 2 ** 256 - 1
    allowance = contr.functions.allowance(address, contract_address).call()
    print(allowance)
    print(allowance)
    if allowance != 0:
        approve_txn = contr.functions.approve(contract_address,
                                                       amountall).build_transaction({
            'from': address,
            'gasPrice': random.randint(1000000000, 1050000000),
            'nonce': web3.eth.get_transaction_count(address),
        })
        signed_approve_txn = web3.eth.account.sign_transaction(approve_txn, private_key)
        approve_txn_hash = web3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)

        print(f"{chain} | TOKEN APPROVED /{approve_txn_hash.hex()}")

    now = datetime.datetime.now()
    now_dt = now.strftime("%d-%m-%Y %H:%M")

    contr_addr = '0xD4888870C8686c748232719051b677791dBDa26D'
    contr_addr_ABI = network_erc20_abi[chain]['veSTG']
    contr = get_erc20_contract(web3, contr_addr, contr_addr_ABI)
    out_decimals = 18
    amount_d = intToDecimal(human_readable, out_decimals)
    amount_str = float_str(human_readable)

    time = 1779926400  # 36 месяцев
    print(balance_wei-(web3.eth.gas_price*326152) )
    print(balance_wei)
    contract_txn = contr.functions.create_lock(amount_d, time).build_transaction({
        'from': address,
        'value': 0,
        'gas': 300000,
        'gasPrice': random.randint(1000000000, 1050000000), # специально ставим 1 гвей, так транза будет дешевле,
        'nonce': web3.eth.get_transaction_count(address)+1,
    })


    signed_txn = web3.eth.account.sign_transaction(contract_txn, private_key)
    print(signed_txn)

    txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    txn_text = txn_hash.hex()

    print(f"\n{now_dt} {address} | УСПЕШНО lock {amount_str} STG tx {txn_text}")


def float_str(amount, decimals=18):
    temp_str = "%0.18f"
    temp_str = temp_str.replace('18', str(decimals))
    text_float = temp_str % amount
    return text_float


def get_erc20_contract(web3, contract_address, ERC20_ABI=''):
    '''Одинаковый ABI для всех ERC20 токенов, в ликвидности могут быть другие ABI '''

    if ERC20_ABI == '':
        ERC20_ABI = json.loads('''[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint256","name":"_initialSupply","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint8","name":"decimals_","type":"uint8"}],"name":"setupDecimals","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]''')

    contract = web3.eth.contract(contract_address, abi=ERC20_ABI)

    return contract








