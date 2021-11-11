class genmem():

    def __init__(self, start, size, readonly):
        self.m = {}
        self.ro = readonly
        for i in range(start, start + size):
            self.m[i] = 0xFF

    def __setitem__(self, addr, data):
        if not self.ro:
            self.m[addr] = data
        return

    def __getitem__(self, addr):
        return self.m[addr]

    def keys(self):
        return self.m.keys()

    def load(self, start, data):
        a = start
        for d in data:
            if a in self.m.keys():
                self.m[a] = d
            a = (a + 1) & 0xFFFF

