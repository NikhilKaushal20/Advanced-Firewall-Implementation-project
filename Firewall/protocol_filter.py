from .base_strategy import FirewallStrategy

class ProtocolFilter(FirewallStrategy):
    def __init__(self):
        self.allowed_protocols = set()

    def allow_protocol(self, protocol):
        self.allowed_protocols.add(protocol)

    def filter(self, packet: dict) -> bool:
        protocol = packet.get("protocol")
        return protocol in self.allowed_protocols
