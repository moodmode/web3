import os
from dotenv import load_dotenv

load_dotenv()


class AvalancheConstants:
    NAME = "Avalanche"
    NATIVE_TOKEN = "AVAX"
    RPC = os.getenv("AVALANCHE_RPC")
    CHAIN_ID = 43114
    LAYERZERO_CHAIN_ID = 106

    # Contracts
    USDC_CONTRACT_ADDRESS = "0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E"
    USDC_DECIMALS = 6

    USDT_CONTRACT_ADDRESS = "0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7"
    USDT_DECIMALS = 6

    STARGATE_ROUTER_CONTRACT_ADDRESS = "0x45A01E4e04F14f7A4a6702c74187c5F6222033cd"

    APPROVE_GAS_LIMIT = 100_000
