import json
from statistics import mean
import time
from web3 import Web3
import requests
import random
from datetime import datetime
import config
import fun
from fun import log
from config import privat_key



current_datetime = datetime.now()
print(f"\n\n {current_datetime}")

wallets = []
with open("wallets.txt", "r") as f:
    for row in f:
        wallet=row.strip()
        if wallet:
            wallets.append(wallet)


i=0
for wallet in wallets:
    i+=1
    
    try:
        web3 = Web3(Web3.HTTPProvider(fun.address['polygon']['rpc'], request_kwargs=config.request_kwargs))
        account = web3.eth.account.from_key(privat_key)
        from_wallet = account.address    
        log(f"I-{i}: Начинаю работу с {wallet}")

    
        wallet = web3.to_checksum_address(wallet)
        gas_price = web3.eth.gas_price
        gas_limit = 21000
        value = web3.to_wei(0.1, 'ether')  # Количество отправляемых ETH
        transaction = {
            'chainId': 137,
            'nonce': web3.eth.get_transaction_count(from_wallet),
            'to': wallet,
            'value': value,
            'gas': gas_limit,
            'gasPrice': gas_price,
        }
 
    
        # Подписываем и отправляем транзакцию
        signed_txn = web3.eth.account.sign_transaction(transaction, privat_key)
        tx_hash = web3.to_hex(web3.eth.send_raw_transaction(signed_txn.rawTransaction))
        tx_result = web3.eth.wait_for_transaction_receipt(tx_hash)

        if tx_result['status'] == 1:
            fun.log_ok(f'SEND  OK: {tx_hash}')
        else:
            fun.log_error(f'SEND  false: {tx_hash}')

    except Exception as error:
        fun.log_error(f"Ошибка: {error}")



    fun.timeOut()










    
log("Ну типа все!")
