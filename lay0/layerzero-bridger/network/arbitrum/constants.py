import os
from dotenv import load_dotenv

load_dotenv()


class ArbitrumConstants:
    NAME = "Arbitrum"
    NATIVE_TOKEN = "ETH"
    RPC = os.getenv("ARBITRUM_RPC")
    CHAIN_ID = 42161
    LAYERZERO_CHAIN_ID = 110

    # Contracts
    USDC_CONTRACT_ADDRESS = "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8"
    USDC_DECIMALS = 6

    USDT_CONTRACT_ADDRESS = "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9"
    USDT_DECIMALS = 6

    STARGATE_ROUTER_CONTRACT_ADDRESS = "0x53Bf833A5d6c4ddA888F69c22C88C9f356a41614"

    APPROVE_GAS_LIMIT = 1_500_000