class Settings:
    def __init__(self):
        self.whitelist = set()
        self.blacklist = set()
        self.default_policy = 'allow'

    def add_to_whitelist(self, entry):
        if entry in self.blacklist:
            self.blacklist.remove(entry)
        self.whitelist.add(entry)

    def add_to_blacklist(self, entry):
        if entry in self.whitelist:
            self.whitelist.remove(entry)
        self.blacklist.add(entry)

    def remove_from_whitelist(self, entry):
        self.whitelist.discard(entry)

    def remove_from_blacklist(self, entry):
        self.blacklist.discard(entry)

    def get_whitelist(self):
        return self.whitelist

    def get_blacklist(self):
        return self.blacklist

    def is_allowed(self, packet):
        entry = f"{packet['ip']},{packet['port']},{packet['protocol']}"
        if entry in self.blacklist:
            return False
        if entry in self.whitelist:
            return True
        return self.default_policy == 'allow'
