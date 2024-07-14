from .base_strategy import FirewallStrategy

class PortFilter(FirewallStrategy):
    def __init__(self):
        self.allowed_ports = set()

    def allow_port(self, port):
        self.allowed_ports.add(port)

    def filter(self, packet: dict) -> bool:
        port = packet.get("port")
        return port in self.allowed_ports
