from web3 import Web3
import time
import random
from decimal import Decimal
from loguru import logger
from tqdm import tqdm
from sys import stderr

time_delay_min = 120  # Min delay between each account
time_delay_max = 180  # Max delay between each account
repeats = 1  # How much runs this script will do. Must be > 0
amount = {"min": 0.0004, "max": 0.00043}  # Amount to bridge min/max. Min value maust be 0.0004 and higher or tx fail!

logger.remove()
logger.add(stderr, format="<lm>{time:YYYY-MM-DD HH:mm:ss}</lm> | <level>{level: <8}</level>| <lw>{message}</lw>")


def harmonyBridge(private_key):
    try:
        web3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/bsc'))
        w3 = Web3(Web3.HTTPProvider('https://bscrpc.com'))
        address_wallet = web3.eth.account.from_key(private_key).address
        logger.info(f'Current account - {address_wallet}')
        addres_contract = Web3.to_checksum_address('0x128aedc7f41ffb82131215e1722d8366faad0cd4')
        abi = '[{"type": "function", "name": "deposit", "inputs": [], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "precrime", "inputs": [], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "decimals", "inputs": [], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "transferOwnership", "inputs": [{"type": "address"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "symbol", "inputs": [], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "forceResumeReceive", "inputs": [{"type": "uint16"}, {"type": "bytes"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "failedMessages", "inputs": [{"type": "uint16"}, {"type": "bytes"}, {"type": "uint64"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "minDstGasLookup", "inputs": [{"type": "uint16"}, {"type": "uint16"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "decreaseAllowance", "inputs": [{"type": "address"}, {"type": "uint256"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "setConfig", "inputs": [{"type": "uint16"}, {"type": "uint16"}, {"type": "uint256"}, {"type": "bytes"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "owner", "inputs": [], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "setTrustedRemote", "inputs": [{"type": "uint16"}, {"type": "bytes"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "nonblockingLzReceive", "inputs": [{"type": "uint16"}, {"type": "bytes"}, {"type": "uint64"}, {"type": "bytes"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "balanceOf", "inputs": [{"type": "address"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "name", "inputs": [], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "approve", "inputs": [{"type": "address"}, {"type": "uint256"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "PT_SEND", "inputs": [], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "setUseCustomAdapterParams", "inputs": [{"type": "bool"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "NO_EXTRA_GAS", "inputs": [], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "retryMessage", "inputs": [{"type": "uint16"}, {"type": "bytes"}, {"type": "uint64"}, {"type": "bytes"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "trustedRemoteLookup", "inputs": [{"type": "uint16"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "increaseAllowance", "inputs": [{"type": "address"}, {"type": "uint256"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "withdraw", "inputs": [{"type": "uint256"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "getTrustedRemoteAddress", "inputs": [{"type": "uint16"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "renounceOwnership", "inputs": [], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "allowance", "inputs": [{"type": "address"}, {"type": "address"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "sendFrom", "inputs": [{"type": "address"}, {"type": "uint16"}, {"type": "bytes"}, {"type": "uint256"}, {"type": "address"}, {"type": "address"}, {"type": "bytes"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "getConfig", "inputs": [{"type": "uint16"}, {"type": "uint16"}, {"type": "address"}, {"type": "uint256"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "transfer", "inputs": [{"type": "address"}, {"type": "uint256"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "lzEndpoint", "inputs": [], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "setMinDstGas", "inputs": [{"type": "uint16"}, {"type": "uint16"}, {"type": "uint256"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "setPrecrime", "inputs": [{"type": "address"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "setTrustedRemoteAddress", "inputs": [{"type": "uint16"}, {"type": "bytes"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "setReceiveVersion", "inputs": [{"type": "uint16"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "totalSupply", "inputs": [], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "isTrustedRemote", "inputs": [{"type": "uint16"}, {"type": "bytes"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "estimateSendFee", "inputs": [{"type": "uint16"}, {"type": "bytes"}, {"type": "uint256"}, {"type": "bool"}, {"type": "bytes"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "supportsInterface", "inputs": [{"type": "bytes4"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "transferFrom", "inputs": [{"type": "address"}, {"type": "address"}, {"type": "uint256"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "setSendVersion", "inputs": [{"type": "uint16"}], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "circulatingSupply", "inputs": [], "outputs": [{"type": "unknown"}]}, {"type": "function", "name": "useCustomAdapterParams", "inputs": [], "outputs": [{"type": "unknown"}]}]'

        _dstChainId = 116
        _tokenId = 213090883261711
        valueRandom = Decimal(round(random.uniform(amount['min'], amount['max']), 7))
        _zroPaymentAddress = '0x0000000000000000000000000000000000000000'
        _adapterParams = "0x000100000000000000000000000000000000000000000000000000000000000aae60"
        contract_data = web3.eth.contract(address=addres_contract, abi=abi)

        bridge_txn = contract_data.functions.sendFrom(address_wallet, _dstChainId, address_wallet, _tokenId,
                                                      address_wallet, _zroPaymentAddress,
                                                      _adapterParams).build_transaction({
            'chainId': 56,
            'value': Web3.to_wei(valueRandom, "ether"),
            'from': address_wallet,
            'gas': 400000,
            'gasPrice': Web3.to_wei(1.1, 'gwei'),
            'nonce': web3.eth.get_transaction_count(address_wallet)
        })

        signed_tx = web3.eth.account.sign_transaction(bridge_txn, private_key)
        raw_tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_hash = web3.to_hex(raw_tx_hash)

        tx_receipt = web3.eth.wait_for_transaction_receipt(raw_tx_hash, timeout=900)
        if tx_receipt.status == 1:
            logger.success(f'Bridge {valueRandom} BNB to Harmony success - https://bscscan.com/tx/{tx_hash}\n')
        else:
            time.sleep(60)
            tx_receipt = w3.eth.get_transaction_receipt(tx_hash)
            status = tx_receipt.status
            if status == 1:
                logger.success(f'Bridge {valueRandom} BNB to Harmony success - https://bscscan.com/tx/{tx_hash}\n')
            else:
                logger.error(f'Bridge {valueRandom} BNB failed: https://bscscan.com/tx/{tx_hash}\n')

    except Exception as error:
        logger.error(error)
        return 0


# if __name__ == '__main__':
#     print()
#     print('This script bridge ~0.0004 BNB to Harmony chain:')
#     print()
#
#     with open("private_key.txt", "r") as f:
#         keys_list = [row.strip() for row in f]
#
#     for i in range(repeats):
#         print(f'Repeat # {i + 1}/{repeats}:')
#         print()
#         keys_list2 = keys_list.copy()
#         while keys_list2:
#             key = keys_list2.pop(0)
#             harmonyBridge(key)
#             sleepDelay = random.randint(time_delay_min, time_delay_max)
#             for i in tqdm(range(sleepDelay), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
#                 time.sleep(1)
#             print()
#     print('Done!')