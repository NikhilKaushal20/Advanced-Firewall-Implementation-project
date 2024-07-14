from .ip_filter import IPFilter
from .port_filter import PortFilter
from .protocol_filter import ProtocolFilter

class StrategyFactory:
    @staticmethod
    def get_strategy(strategy_type):
        if strategy_type == "ip_filter":
            return IPFilter()
        elif strategy_type == "port_filter":
            return PortFilter()
        elif strategy_type == "protocol_filter":
            return ProtocolFilter()
        else:
            raise ValueError(f"Unknown strategy type: {strategy_type}")
