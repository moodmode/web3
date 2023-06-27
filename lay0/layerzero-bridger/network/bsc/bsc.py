import logging

from network.bsc.constants import BSCConstants
from network.network import EVMNetwork
from stargate import StargateConstants
from utility import Stablecoin

logger = logging.getLogger(__name__)


class BSC(EVMNetwork):

    def __init__(self):
        supported_stablecoins = {
            'USDT': Stablecoin('USDT', BSCConstants.USDT_CONTRACT_ADDRESS, BSCConstants.USDT_DECIMALS,
                               BSCConstants.LAYERZERO_CHAIN_ID, StargateConstants.POOLS['USDT']),
            'BUSD': Stablecoin('BUSD', BSCConstants.BUSD_CONTRACT_ADDRESS, BSCConstants.BUSD_DECIMALS,
                               BSCConstants.LAYERZERO_CHAIN_ID, StargateConstants.POOLS['BUSD'])
        }

        super().__init__(BSCConstants.NAME, BSCConstants.NATIVE_TOKEN, BSCConstants.RPC,
                         BSCConstants.LAYERZERO_CHAIN_ID, BSCConstants.STARGATE_ROUTER_CONTRACT_ADDRESS,
                         supported_stablecoins)

    def get_approve_gas_limit(self) -> int:
        return BSCConstants.APPROVE_GAS_LIMIT

    def get_transaction_gas_params(self) -> dict:
        gas_params = {
            'gasPrice': self.get_current_gas()
        }

        logger.debug(f"{self.name} gas params fetched. Params: {gas_params}")

        return gas_params
