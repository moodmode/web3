import random
import sys
import time

from web3 import Web3

from corebridge import Corebridge, to_core_bridge
from harmony import harmonyBridge
from helping_commands import get_accound_addres
from sgt_stake import stake_stg
from swap_bnb_1inch import swap_stg
from swap_starget import swap_stable_coin_on_stargate


def main():

    with open("private_keys.txt", "r") as f:
        keys_list = [row.strip() for row in f]



    for private_key in keys_list:
        address = get_accound_addres(private_key)
        print(address)
        # print(f"начинаю работу с {address} покупка стг")
        #swap_stg(private_key,address) # покупка стг
        # print(f"начинаю работу с {address} закидываю стг с стейкинг")
        # stake_stg(private_key,address) # стаке стг
        # harmonyBridge(private_key) # рабоатет
        to_core_bridge(private_key)  # работает



    # Corebridge()  # usdt(bsc)  свапает 10 процентов от баланса usdt bsc




if __name__ == '__main__':
    main()


