from Firewall.strategy_factory import StrategyFactory
from Config.settings import Settings

def main():
    settings = Settings()
    default_policy = settings.get_default_policy()
    ip_filter = StrategyFactory.get_strategy("ip_filter")
    port_filter = StrategyFactory.get_strategy("port_filter")
    protocol_filter = StrategyFactory.get_strategy("protocol_filter")

    print("Advanced Firewall is running...")
    while True:
        packet = input("Enter packet details as a dictionary (or type 'exit' to quit): ")
        if packet.lower() == 'exit':
            break
        try:
            packet = eval(packet)
            if ip_filter.filter(packet) and port_filter.filter(packet) and protocol_filter.filter(packet):
                print("Packet allowed")
            else:
                print("Packet denied")
        except Exception as e:
            print("Invalid packet format:", e)

if __name__ == "__main__":
    main()
