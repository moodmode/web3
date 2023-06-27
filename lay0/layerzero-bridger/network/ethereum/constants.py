import os
from dotenv import load_dotenv

load_dotenv()


class EthereumConstants:
    NAME = "Ethereum"
    NATIVE_TOKEN = "ETH"
    RPC = os.getenv("ETHEREUM_RPC")
    CHAIN_ID = 1
    LAYERZERO_CHAIN_ID = 101

    # Contracts
    USDC_CONTRACT_ADDRESS = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
    USDC_DECIMALS = 6

    USDT_CONTRACT_ADDRESS = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
    USDT_DECIMALS = 6

    STARGATE_ROUTER_CONTRACT_ADDRESS = "0x8731d54E9D02c286767d56ac03e8037C07e01e98"

    APPROVE_GAS_LIMIT = 100_000
