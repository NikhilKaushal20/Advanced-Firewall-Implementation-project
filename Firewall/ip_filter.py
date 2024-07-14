from Config.settings import Settings

class IPFilter:
    def __init__(self):
        self.settings = Settings()
        self.whitelist = self.settings.get_whitelist()
        self.blacklist = self.settings.get_blacklist()

    def filter(self, packet):
        ip = packet.get('ip')
        if ip in self.blacklist:
            return False
        if ip in self.whitelist:
            return True
        return self.settings.default_policy == 'allow'
