import random
import time

from web3 import Web3

from config import DATA, bnb_min_stg_buy, bnb_max_stg_buy
from helping_commands import intToDecimal, get_api_call_data


def swap_stg(privatekey,wallet  ):
    chain='bsc'
    base_url = 'https://rpc.ankr.com/bsc'
    inch_version = 5
    divider = 1
    rpc = DATA['bsc']['rpc']
    web3 = Web3(Web3.HTTPProvider(rpc))

    chain_id = web3.eth.chain_id
    print(chain_id)
    from_token_address=''
    to_token_address=''
    bnb_value = round(random.uniform(bnb_min_stg_buy, bnb_max_stg_buy), 8)
    # bnb_value = round(random.uniform(0.0001, 0.003), 8)

    if from_token_address == '':
        from_token_address = '0x0000000000000000000000000000000000001000'
        from_decimals = 18
        from_symbol = DATA['bsc']['token']


    if to_token_address == '':
        to_token_address = '0xB0D502E938ed5f4df2E681fE6E419ff29631d62b'
        to_symbol = DATA['bsc']['token']

    amount_to_swap = intToDecimal(bnb_value, from_decimals)
    slippage = 3
    _1inchurl = f'{base_url}/v{inch_version}.0/{chain_id}/swap?fromTokenAddress={from_token_address}&toTokenAddress={to_token_address}&amount={amount_to_swap}&fromAddress={wallet}&slippage={slippage}'
    print(_1inchurl)
    try:
        json_data = get_api_call_data(_1inchurl)
        print(json_data)
    except:
        print(f'на кошельке {wallet} не хватает бнб')
        return False
    print(json_data['tx'])
    tx = json_data['tx']

    tx['chainId'] = chain_id
    tx['nonce'] = web3.eth.get_transaction_count(wallet)
    tx['to'] = Web3.to_checksum_address(tx['to'])
    tx['gasPrice'] = int(tx['gasPrice'])
    tx['gas'] = int(int(tx['gas']) / divider)
    tx['value'] = int(tx['value'])

    if chain == 'bsc':
        tx['gasPrice'] = random.randint(1000000000, 1050000000)  # специально ставим 1 гвей, так транза будет дешевле

    signed_tx = web3.eth.account.sign_transaction(tx, privatekey)
    raw_tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = web3.to_hex(raw_tx_hash)

    #покупка 0.5 usdt в сети bsc
    amount_to_swap=amount_to_swap/2
    to_token_address='0x55d398326f99059ff775485246999027b3197955'
    _1inchurl = f'{base_url}/v{inch_version}.0/{chain_id}/swap?fromTokenAddress={from_token_address}&toTokenAddress={to_token_address}&amount={amount_to_swap}&fromAddress={wallet}&slippage={slippage}'
    print(_1inchurl)
    try:
        json_data = get_api_call_data(_1inchurl)
        print(json_data)
    except:
        print(f'на кошельке {wallet} не хватает бнб')
        return False
    print(json_data['tx'])
    tx = json_data['tx']

    tx['chainId'] = chain_id
    tx['nonce'] = web3.eth.get_transaction_count(wallet)
    tx['to'] = Web3.to_checksum_address(tx['to'])
    tx['gasPrice'] = int(tx['gasPrice'])
    tx['gas'] = int(int(tx['gas']) / divider)
    tx['value'] = int(tx['value'])

    if chain == 'bsc':
        tx['gasPrice'] = random.randint(1000000000, 1050000000)  # специально ставим 1 гвей, так транза будет дешевле

    signed_tx = web3.eth.account.sign_transaction(tx, privatekey)
    raw_tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = web3.to_hex(raw_tx_hash)


def check_status_tx(chain, tx_hash):
    max_time_check_tx_status = 100
    start_time_stamp = int(time.time())

    while True:
        try:

            rpc_chain   = DATA[chain]['rpc']
            web3        = Web3(Web3.HTTPProvider(rpc_chain))
            status_     = web3.eth.get_transaction_receipt(tx_hash)
            status      = status_["status"]

            if status in [0, 1]:
                return status

        except Exception as error:

            time_stamp = int(time.time())
            if time_stamp-start_time_stamp > max_time_check_tx_status:

                return 1
            time.sleep(1)