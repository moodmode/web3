import json
from random import randint, shuffle
from time import sleep
from web3 import Web3
from web3.auto import w3
import random
import time
from tqdm import tqdm
import traceback
from web3 import Account
from termcolor import cprint

MIN_SLEEP = 60  # минимальное время между аккаунтами в секундах
MAX_SLEEP = 180 # максимальное
POVTOR = 1 # количество повторений

# Core Router
bnb_address = w3.to_checksum_address('0x52e75d318cfb31f9a2edfa2dfee26b161255b233')
core_address = w3.to_checksum_address('0xA4218e1F39DA4AaDaC971066458Db56e901bcbdE')

# RPCs
bnb_w3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/bsc'))
core_w3 = Web3(Web3.HTTPProvider('https://rpc.coredao.org'))

# ABIs
bnb_abi = json.load(open('./abis/bnb_abi.json'))
usdt_abi = json.load(open('./abis/usdt_abi.json'))
core_abi = '[{"inputs":[{"name":"_endpoint","internalType":"address","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"indexed":false,"name":"_srcChainId","internalType":"uint16","type":"uint16"},{"indexed":false,"name":"_srcAddress","internalType":"bytes","type":"bytes"},{"indexed":false,"name":"_nonce","internalType":"uint64","type":"uint64"},{"indexed":false,"name":"_payload","internalType":"bytes","type":"bytes"},{"indexed":false,"name":"_reason","internalType":"bytes","type":"bytes"}],"name":"MessageFailed","anonymous":false,"type":"event"},{"inputs":[{"indexed":true,"name":"previousOwner","internalType":"address","type":"address"},{"indexed":true,"name":"newOwner","internalType":"address","type":"address"}],"name":"OwnershipTransferred","anonymous":false,"type":"event"},{"inputs":[{"indexed":false,"name":"localToken","internalType":"address","type":"address"},{"indexed":false,"name":"remoteChainId","internalType":"uint16","type":"uint16"},{"indexed":false,"name":"remoteToken","internalType":"address","type":"address"}],"name":"RegisterToken","anonymous":false,"type":"event"},{"inputs":[{"indexed":false,"name":"_srcChainId","internalType":"uint16","type":"uint16"},{"indexed":false,"name":"_srcAddress","internalType":"bytes","type":"bytes"},{"indexed":false,"name":"_nonce","internalType":"uint64","type":"uint64"},{"indexed":false,"name":"_payloadHash","internalType":"bytes32","type":"bytes32"}],"name":"RetryMessageSuccess","anonymous":false,"type":"event"},{"inputs":[{"indexed":false,"name":"_dstChainId","internalType":"uint16","type":"uint16"},{"indexed":false,"name":"_type","internalType":"uint16","type":"uint16"},{"indexed":false,"name":"_minDstGas","internalType":"uint256","type":"uint256"}],"name":"SetMinDstGas","anonymous":false,"type":"event"},{"inputs":[{"indexed":false,"name":"precrime","internalType":"address","type":"address"}],"name":"SetPrecrime","anonymous":false,"type":"event"},{"inputs":[{"indexed":false,"name":"_remoteChainId","internalType":"uint16","type":"uint16"},{"indexed":false,"name":"_path","internalType":"bytes","type":"bytes"}],"name":"SetTrustedRemote","anonymous":false,"type":"event"},{"inputs":[{"indexed":false,"name":"_remoteChainId","internalType":"uint16","type":"uint16"},{"indexed":false,"name":"_remoteAddress","internalType":"bytes","type":"bytes"}],"name":"SetTrustedRemoteAddress","anonymous":false,"type":"event"},{"inputs":[{"indexed":false,"name":"useCustomAdapterParams","internalType":"bool","type":"bool"}],"name":"SetUseCustomAdapterParams","anonymous":false,"type":"event"},{"inputs":[{"indexed":false,"name":"withdrawalFeeBps","internalType":"uint16","type":"uint16"}],"name":"SetWithdrawalFeeBps","anonymous":false,"type":"event"},{"inputs":[{"indexed":false,"name":"localToken","internalType":"address","type":"address"},{"indexed":false,"name":"remoteToken","internalType":"address","type":"address"},{"indexed":false,"name":"remoteChainId","internalType":"uint16","type":"uint16"},{"indexed":false,"name":"to","internalType":"address","type":"address"},{"indexed":false,"name":"amount","internalType":"uint256","type":"uint256"}],"name":"UnwrapToken","anonymous":false,"type":"event"},{"inputs":[{"indexed":false,"name":"localToken","internalType":"address","type":"address"},{"indexed":false,"name":"remoteToken","internalType":"address","type":"address"},{"indexed":false,"name":"remoteChainId","internalType":"uint16","type":"uint16"},{"indexed":false,"name":"to","internalType":"address","type":"address"},{"indexed":false,"name":"amount","internalType":"uint256","type":"uint256"}],"name":"WrapToken","anonymous":false,"type":"event"},{"outputs":[{"name":"","internalType":"uint8","type":"uint8"}],"inputs":[],"name":"PT_MINT","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"uint8","type":"uint8"}],"inputs":[],"name":"PT_UNLOCK","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"uint16","type":"uint16"}],"inputs":[],"name":"TOTAL_BPS","stateMutability":"view","type":"function"},{"outputs":[],"inputs":[{"name":"localToken","internalType":"address","type":"address"},{"name":"remoteChainId","internalType":"uint16","type":"uint16"},{"name":"amount","internalType":"uint256","type":"uint256"},{"name":"to","internalType":"address","type":"address"},{"name":"unwrapWeth","internalType":"bool","type":"bool"},{"components":[{"name":"refundAddress","internalType":"address payable","type":"address"},{"name":"zroPaymentAddress","internalType":"address","type":"address"}],"name":"callParams","internalType":"struct LzLib.CallParams","type":"tuple"},{"name":"adapterParams","internalType":"bytes","type":"bytes"}],"name":"bridge","stateMutability":"payable","type":"function"},{"outputs":[{"name":"nativeFee","internalType":"uint256","type":"uint256"},{"name":"zroFee","internalType":"uint256","type":"uint256"}],"inputs":[{"name":"remoteChainId","internalType":"uint16","type":"uint16"},{"name":"useZro","internalType":"bool","type":"bool"},{"name":"adapterParams","internalType":"bytes","type":"bytes"}],"name":"estimateBridgeFee","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"bytes32","type":"bytes32"}],"inputs":[{"name":"","internalType":"uint16","type":"uint16"},{"name":"","internalType":"bytes","type":"bytes"},{"name":"","internalType":"uint64","type":"uint64"}],"name":"failedMessages","stateMutability":"view","type":"function"},{"outputs":[],"inputs":[{"name":"_srcChainId","internalType":"uint16","type":"uint16"},{"name":"_srcAddress","internalType":"bytes","type":"bytes"}],"name":"forceResumeReceive","stateMutability":"nonpayable","type":"function"},{"outputs":[{"name":"","internalType":"bytes","type":"bytes"}],"inputs":[{"name":"_version","internalType":"uint16","type":"uint16"},{"name":"_chainId","internalType":"uint16","type":"uint16"},{"name":"","internalType":"address","type":"address"},{"name":"_configType","internalType":"uint256","type":"uint256"}],"name":"getConfig","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"bytes","type":"bytes"}],"inputs":[{"name":"_remoteChainId","internalType":"uint16","type":"uint16"}],"name":"getTrustedRemoteAddress","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"bool","type":"bool"}],"inputs":[{"name":"_srcChainId","internalType":"uint16","type":"uint16"},{"name":"_srcAddress","internalType":"bytes","type":"bytes"}],"name":"isTrustedRemote","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"address","type":"address"}],"inputs":[{"name":"","internalType":"address","type":"address"},{"name":"","internalType":"uint16","type":"uint16"}],"name":"localToRemote","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"contract ILayerZeroEndpoint","type":"address"}],"inputs":[],"name":"lzEndpoint","stateMutability":"view","type":"function"},{"outputs":[],"inputs":[{"name":"_srcChainId","internalType":"uint16","type":"uint16"},{"name":"_srcAddress","internalType":"bytes","type":"bytes"},{"name":"_nonce","internalType":"uint64","type":"uint64"},{"name":"_payload","internalType":"bytes","type":"bytes"}],"name":"lzReceive","stateMutability":"nonpayable","type":"function"},{"outputs":[{"name":"","internalType":"uint256","type":"uint256"}],"inputs":[{"name":"","internalType":"uint16","type":"uint16"},{"name":"","internalType":"uint16","type":"uint16"}],"name":"minDstGasLookup","stateMutability":"view","type":"function"},{"outputs":[],"inputs":[{"name":"_srcChainId","internalType":"uint16","type":"uint16"},{"name":"_srcAddress","internalType":"bytes","type":"bytes"},{"name":"_nonce","internalType":"uint64","type":"uint64"},{"name":"_payload","internalType":"bytes","type":"bytes"}],"name":"nonblockingLzReceive","stateMutability":"nonpayable","type":"function"},{"outputs":[{"name":"","internalType":"address","type":"address"}],"inputs":[],"name":"owner","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"address","type":"address"}],"inputs":[],"name":"precrime","stateMutability":"view","type":"function"},{"outputs":[],"inputs":[{"name":"localToken","internalType":"address","type":"address"},{"name":"remoteChainId","internalType":"uint16","type":"uint16"},{"name":"remoteToken","internalType":"address","type":"address"}],"name":"registerToken","stateMutability":"nonpayable","type":"function"},{"outputs":[{"name":"","internalType":"address","type":"address"}],"inputs":[{"name":"","internalType":"address","type":"address"},{"name":"","internalType":"uint16","type":"uint16"}],"name":"remoteToLocal","stateMutability":"view","type":"function"},{"outputs":[],"inputs":[],"name":"renounceOwnership","stateMutability":"nonpayable","type":"function"},{"outputs":[],"inputs":[{"name":"_srcChainId","internalType":"uint16","type":"uint16"},{"name":"_srcAddress","internalType":"bytes","type":"bytes"},{"name":"_nonce","internalType":"uint64","type":"uint64"},{"name":"_payload","internalType":"bytes","type":"bytes"}],"name":"retryMessage","stateMutability":"payable","type":"function"},{"outputs":[],"inputs":[{"name":"_version","internalType":"uint16","type":"uint16"},{"name":"_chainId","internalType":"uint16","type":"uint16"},{"name":"_configType","internalType":"uint256","type":"uint256"},{"name":"_config","internalType":"bytes","type":"bytes"}],"name":"setConfig","stateMutability":"nonpayable","type":"function"},{"outputs":[],"inputs":[{"name":"_dstChainId","internalType":"uint16","type":"uint16"},{"name":"_packetType","internalType":"uint16","type":"uint16"},{"name":"_minGas","internalType":"uint256","type":"uint256"}],"name":"setMinDstGas","stateMutability":"nonpayable","type":"function"},{"outputs":[],"inputs":[{"name":"_precrime","internalType":"address","type":"address"}],"name":"setPrecrime","stateMutability":"nonpayable","type":"function"},{"outputs":[],"inputs":[{"name":"_version","internalType":"uint16","type":"uint16"}],"name":"setReceiveVersion","stateMutability":"nonpayable","type":"function"},{"outputs":[],"inputs":[{"name":"_version","internalType":"uint16","type":"uint16"}],"name":"setSendVersion","stateMutability":"nonpayable","type":"function"},{"outputs":[],"inputs":[{"name":"_srcChainId","internalType":"uint16","type":"uint16"},{"name":"_path","internalType":"bytes","type":"bytes"}],"name":"setTrustedRemote","stateMutability":"nonpayable","type":"function"},{"outputs":[],"inputs":[{"name":"_remoteChainId","internalType":"uint16","type":"uint16"},{"name":"_remoteAddress","internalType":"bytes","type":"bytes"}],"name":"setTrustedRemoteAddress","stateMutability":"nonpayable","type":"function"},{"outputs":[],"inputs":[{"name":"_useCustomAdapterParams","internalType":"bool","type":"bool"}],"name":"setUseCustomAdapterParams","stateMutability":"nonpayable","type":"function"},{"outputs":[],"inputs":[{"name":"_withdrawalFeeBps","internalType":"uint16","type":"uint16"}],"name":"setWithdrawalFeeBps","stateMutability":"nonpayable","type":"function"},{"outputs":[{"name":"","internalType":"uint256","type":"uint256"}],"inputs":[{"name":"","internalType":"uint16","type":"uint16"},{"name":"","internalType":"address","type":"address"}],"name":"totalValueLocked","stateMutability":"view","type":"function"},{"outputs":[],"inputs":[{"name":"newOwner","internalType":"address","type":"address"}],"name":"transferOwnership","stateMutability":"nonpayable","type":"function"},{"outputs":[{"name":"","internalType":"bytes","type":"bytes"}],"inputs":[{"name":"","internalType":"uint16","type":"uint16"}],"name":"trustedRemoteLookup","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"bool","type":"bool"}],"inputs":[],"name":"useCustomAdapterParams","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"uint16","type":"uint16"}],"inputs":[],"name":"withdrawalFeeBps","stateMutability":"view","type":"function"}]'
usdt_abi_core = '[{"inputs":[{"name":"_bridge","internalType":"address","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"indexed":true,"name":"owner","internalType":"address","type":"address"},{"indexed":true,"name":"spender","internalType":"address","type":"address"},{"indexed":false,"name":"value","internalType":"uint256","type":"uint256"}],"name":"Approval","anonymous":false,"type":"event"},{"inputs":[{"indexed":true,"name":"from","internalType":"address","type":"address"},{"indexed":true,"name":"to","internalType":"address","type":"address"},{"indexed":false,"name":"value","internalType":"uint256","type":"uint256"}],"name":"Transfer","anonymous":false,"type":"event"},{"outputs":[{"name":"","internalType":"uint256","type":"uint256"}],"inputs":[{"name":"owner","internalType":"address","type":"address"},{"name":"spender","internalType":"address","type":"address"}],"name":"allowance","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"bool","type":"bool"}],"inputs":[{"name":"spender","internalType":"address","type":"address"},{"name":"amount","internalType":"uint256","type":"uint256"}],"name":"approve","stateMutability":"nonpayable","type":"function"},{"outputs":[{"name":"","internalType":"uint256","type":"uint256"}],"inputs":[{"name":"account","internalType":"address","type":"address"}],"name":"balanceOf","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"address","type":"address"}],"inputs":[],"name":"bridge","stateMutability":"view","type":"function"},{"outputs":[],"inputs":[{"name":"_from","internalType":"address","type":"address"},{"name":"_amount","internalType":"uint256","type":"uint256"}],"name":"burn","stateMutability":"nonpayable","type":"function"},{"outputs":[{"name":"","internalType":"uint8","type":"uint8"}],"inputs":[],"name":"decimals","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"bool","type":"bool"}],"inputs":[{"name":"spender","internalType":"address","type":"address"},{"name":"subtractedValue","internalType":"uint256","type":"uint256"}],"name":"decreaseAllowance","stateMutability":"nonpayable","type":"function"},{"outputs":[{"name":"","internalType":"bool","type":"bool"}],"inputs":[{"name":"spender","internalType":"address","type":"address"},{"name":"addedValue","internalType":"uint256","type":"uint256"}],"name":"increaseAllowance","stateMutability":"nonpayable","type":"function"},{"outputs":[],"inputs":[{"name":"_to","internalType":"address","type":"address"},{"name":"_amount","internalType":"uint256","type":"uint256"}],"name":"mint","stateMutability":"nonpayable","type":"function"},{"outputs":[{"name":"","internalType":"string","type":"string"}],"inputs":[],"name":"name","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"string","type":"string"}],"inputs":[],"name":"symbol","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"uint256","type":"uint256"}],"inputs":[],"name":"totalSupply","stateMutability":"view","type":"function"},{"outputs":[{"name":"","internalType":"bool","type":"bool"}],"inputs":[{"name":"to","internalType":"address","type":"address"},{"name":"amount","internalType":"uint256","type":"uint256"}],"name":"transfer","stateMutability":"nonpayable","type":"function"},{"outputs":[{"name":"","internalType":"bool","type":"bool"}],"inputs":[{"name":"from","internalType":"address","type":"address"},{"name":"to","internalType":"address","type":"address"},{"name":"amount","internalType":"uint256","type":"uint256"}],"name":"transferFrom","stateMutability":"nonpayable","type":"function"}]'


# contracts
usdt_bnb_address = w3.to_checksum_address('0x55d398326f99059ff775485246999027b3197955')
usdt_core_address = w3.to_checksum_address('0x900101d06a7426441ae63e9ab3b9b0f63be145f1')

# Init contracts
bnb_contract = bnb_w3.eth.contract(address=bnb_address, abi=bnb_abi)
usdt_bnb_contract = bnb_w3.eth.contract(address=usdt_bnb_address, abi=usdt_abi)

core_contract = core_w3.eth.contract(address=core_address, abi=core_abi)
usdt_core_contract = core_w3.eth.contract(address=usdt_core_address, abi=usdt_abi_core)

def sleeping(from_sleep, to_sleep):
    x = random.randint(from_sleep, to_sleep)
    for _ in tqdm(range(x), desc='sleep ', bar_format='{desc}: {n_fmt}/{total_fmt}'):
        time.sleep(1)

def to_bnb_bridge(pk):
    address = core_w3.eth.account.from_key(pk).address
    nonce = core_w3.eth.get_transaction_count(address)
    fees = core_contract.functions.estimateBridgeFee(102, False, "0x").call()

    fee = fees[0]
    gasrand = randint(200000, 250000)

    # Allowance
    allowance = usdt_core_contract.functions.allowance(address, core_address).call()
    amount = usdt_core_contract.functions.balanceOf(address).call()
    if allowance < amount:
        amountNew = 2 ** 256 - 1
        approve_txn = usdt_core_contract.functions.approve(core_address, amountNew).build_transaction({
            'from': address,
            'gas': gasrand,
            'gasPrice': core_w3.eth.gas_price,
            'nonce': nonce,
        })
        signed_approve_txn = core_w3.eth.account.sign_transaction(approve_txn, pk)
        approve_txn_hash = core_w3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)

        print(f"BSC | USDT APPROVED https://scan.coredao.org/tx/{approve_txn_hash.hex()}")
        status = core_w3.eth.wait_for_transaction_receipt(approve_txn_hash, timeout=60).status
        if status == 1:
            cprint('Successfully APPROVED!', 'green')
        nonce += 1
        time.sleep(20)

    # Core -> BSC
    retry = 0
    while True:
        try:
            token = usdt_core_address
            chainID = 102
            amountLD = usdt_core_contract.functions.balanceOf(address).call()
            amountLD_New = amountLD * 10 // 100  # 10% свапаем
            to = address
            unwrapWeth = False
            callParam = [address, '0x0000000000000000000000000000000000000000']
            adaptParam = '0x'

            swap_txn = core_contract.functions.bridge(token, chainID, amountLD_New, to, unwrapWeth, callParam, adaptParam)
            swap_txn = swap_txn.build_transaction({
                "chainId": core_w3.eth.chain_id,
                'from': address,
                'value': fee,
                'gasPrice': core_w3.eth.gas_price,
                'nonce': nonce,
            })
            gasLimit = core_w3.eth.estimate_gas(swap_txn)
            swap_txn['gas'] = int(gasLimit + gasLimit * 0.5)
            signed_swap_txn = core_w3.eth.account.sign_transaction(swap_txn, pk)
            swap_txn_hash = core_w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)
            print(f'https://scan.coredao.org/tx/{swap_txn_hash.hex()}')
            status = core_w3.eth.wait_for_transaction_receipt(swap_txn_hash, timeout=60).status
            if status != 1:
                raise ValueError(f'bad tx status: {status}')
            else:
                cprint(f'[{address}]Successfully bridge!', 'green')
                return True
        except Exception as err:
            retry += 1
            cprint(f'[{address}] bridge error: {type(err).__name__} {err}', 'red')
            if retry < POVTOR:
                cprint(f'[{retry}/{POVTOR}] trying again...', 'yellow')
                sleeping(15, 15)
            else:
                return False

def to_core_bridge(pk):
    address = bnb_w3.eth.account.from_key(pk).address
    nonce = bnb_w3.eth.get_transaction_count(address)
    fees = bnb_contract.functions.estimateBridgeFee(True, "0x").call()

    fee = fees[0]
    print(fee)
    gasrand = randint(300000, 350000)

    # Allowance
    allowance = usdt_bnb_contract.functions.allowance(address, bnb_address).call()
    amount = usdt_bnb_contract.functions.balanceOf(address).call()
    if allowance < amount:
        amountNew = 2 ** 256 - 1
        approve_txn = usdt_bnb_contract.functions.approve(bnb_address, amountNew).build_transaction({
            'from': address,
            'gas': gasrand,
            'gasPrice': random.randint(1000000000, 1050000000),
            'nonce': nonce,
        })
        signed_approve_txn = bnb_w3.eth.account.sign_transaction(approve_txn, pk)
        approve_txn_hash = bnb_w3.eth.send_raw_transaction(signed_approve_txn.rawTransaction)

        print(f"BSC | USDT APPROVED https://bscscan.com/tx/{approve_txn_hash.hex()}")
        status = bnb_w3.eth.wait_for_transaction_receipt(approve_txn_hash, timeout=60).status
        if status == 1:
            cprint('Successfully APPROVED!', 'green')
        nonce += 1
        time.sleep(20)

    # BSC -> Core
    retry = 0
    while True:
        try:
            token = usdt_bnb_address
            amountLD = usdt_bnb_contract.functions.balanceOf(address).call() #баланс USDT
            print(amountLD)
            amountLD_New = amountLD * 1//100 # 1% свапаем
            to = address
            callParam = [address, '0x0000000000000000000000000000000000000000']
            adaptParam = '0x'

            swap_txn = bnb_contract.functions.bridge(token, amountLD_New, to, callParam, adaptParam).build_transaction({
                'from': address,
                'value': fee,
                'gasPrice': random.randint(1000000000, 1050000000),
                'nonce': nonce,
            })
            gasLimit = bnb_w3.eth.estimate_gas(swap_txn)
            swap_txn['gas'] = int(gasLimit + gasLimit * 0.5)
            signed_swap_txn = bnb_w3.eth.account.sign_transaction(swap_txn, pk)
            swap_txn_hash = bnb_w3.eth.send_raw_transaction(signed_swap_txn.rawTransaction)
            print(f'https://bscscan.com/tx/{swap_txn_hash.hex()}')
            status = bnb_w3.eth.wait_for_transaction_receipt(swap_txn_hash, timeout=60).status
            if status != 1:
                raise ValueError(f'bad tx status: {status}')
            else:
                cprint(f'[{address}] Successfully bridge!', 'green')
                return True
        except Exception as err:
            retry += 1
            cprint(f'[{address}] bridge error: {type(err).__name__} {err}', 'red')
            if retry < POVTOR:
                cprint(f'[{retry}/{POVTOR}] trying again...', 'yellow')
                sleeping(15, 15)
            else:
                return False

def Corebridge():
    while True:
        # print('Введи номер направление: ')
        # print('1. BSC -> Core')
        # print('2. Core -> BSC')
        # print('0. Закончить работу')
        marshrut = 1
        if marshrut == 0:
            break
        with open('private_keys.txt') as f:
            p_keys = f.read().splitlines()
        max_akkaunt = p_keys.__len__()

        if marshrut == 1:
            cprint(f"=====================================================", 'yellow')
            cprint(f"============== Начинаем бриджи в Core  ==============", 'yellow')
            cprint(f"=====================================================", 'yellow')
        else:
            cprint(f"=========================================================", 'yellow')
            cprint(f"==============  Начинаем бриджи в BSC    ================", 'yellow')
            cprint(f"=========================================================", 'yellow')

        shuffle(p_keys)  # мешаем
        for pk in p_keys:

            tek_akk = tek_akk + 1
            if marshrut == 1:
                to_core_bridge(pk)
            else:
                to_bnb_bridge(pk)
            to_sleep = randint(MIN_SLEEP, MAX_SLEEP)
            if tek_akk < max_akkaunt:
                print(f'Сон {to_sleep} сек до след. аккаунта..')
                sleeping(to_sleep, to_sleep)
                break
        to_sleep = randint(MIN_SLEEP, MAX_SLEEP)
        sleeping(to_sleep * 2, to_sleep)



