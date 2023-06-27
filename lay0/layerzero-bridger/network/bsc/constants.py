import os
from dotenv import load_dotenv

load_dotenv()


class BSCConstants:
    NAME = "BSC"
    NATIVE_TOKEN = "BNB"
    RPC = os.getenv("BSC_RPC")
    CHAIN_ID = 56
    LAYERZERO_CHAIN_ID = 102

    # Contracts
    BUSD_CONTRACT_ADDRESS = "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56"
    BUSD_DECIMALS = 18

    USDT_CONTRACT_ADDRESS = "0x55d398326f99059fF775485246999027B3197955"
    USDT_DECIMALS = 18

    STARGATE_ROUTER_CONTRACT_ADDRESS = "0x4a364f8c717cAAD9A442737Eb7b8A55cc6cf18D8"

    APPROVE_GAS_LIMIT = 100_000
