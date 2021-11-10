#
# Z80 block instructions
#


from utils import *


class block:

    def __init__(self, parent):
        self.c = parent

    def ldi(self, disass=False):
        bc = word(self.c.r[rpBC] - 1)
        de = self.c.r[rpDE]
        hl = self.c.r[rpHL]
        d = self.c.rdmem(hl)
        self.c.wrmem(de, d)
        self.c.r[rpHL] = word(hl + 1)
        self.c.r[rpDE] = word(de + 1)
        self.c.r[rpBC] = bc
        d += self.c.r[rA]
        f = self.c.r[rF] & 0xC1
        f |= ((d & 0x02) << 4) | (d & 0x08)
        f |= 0x04 if bc else 0
        self.c.r[rF] = f
        if not disass:
            return
        return "LDI"

    def ldir(self, disass=False):
        bc = word(self.c.r[rpBC] - 1)
        de = self.c.r[rpDE]
        hl = self.c.r[rpHL]
        d = self.c.rdmem(hl)
        self.c.wrmem(de, d)
        self.c.r[rpHL] = word(hl + 1)
        self.c.r[rpDE] = word(de + 1)
        self.c.r[rpBC] = bc
        d += self.c.r[rA]
        f = self.c.r[rF] & 0xC1
        f |= ((d & 0x02) << 4) | (d & 0x08)
        f |= 0x04 if bc else 0
        self.c.r[rF] = f
        if bc:
            self.c.r[rpPC] = word(self.c.r[rpPC] - 2)
        if not disass:
            return
        return "LDIR"

    def ldd(self, disass=False):
        bc = word(self.c.r[rpBC] - 1)
        de = self.c.r[rpDE]
        hl = self.c.r[rpHL]
        d = self.c.rdmem(hl)
        self.c.wrmem(de, d)
        self.c.r[rpHL] = word(hl - 1)
        self.c.r[rpDE] = word(de - 1)
        self.c.r[rpBC] = bc
        d += self.c.r[rA]
        f = self.c.r[rF] & 0xC1
        f |= ((d & 0x02) << 4) | (d & 0x08)
        f |= 0x04 if bc else 0
        self.c.r[rF] = f
        if not disass:
            return
        return "LDD"

    def lddr(self, disass=False):
        bc = word(self.c.r[rpBC] - 1)
        de = self.c.r[rpDE]
        hl = self.c.r[rpHL]
        d = self.c.rdmem(hl)
        self.c.wrmem(de, d)
        self.c.r[rpHL] = word(hl - 1)
        self.c.r[rpDE] = word(de - 1)
        self.c.r[rpBC] = bc
        d += self.c.r[rA]
        f = self.c.r[rF] & 0xC1
        f |= ((d & 0x02) << 4) | (d & 0x08)
        f |= 0x04 if bc else 0
        self.c.r[rF] = f
        if bc:
            self.c.r[rpPC] = word(self.c.r[rpPC] - 2)
        if not disass:
            return
        return "LDDR"

    def cpi(self, disass=False):
        bc = word(self.c.r[rpBC] - 1)
        hl = self.c.r[rpHL]
        r = sub8(self.c.r[rA], self.c.rdmem(hl), 0)
        t = r[0] - ((r[1] & 0x10) >> 4)
        f = 0x06 if bc else 0x02
        f |= (t & 0x08) | ((t & 0x02) << 4) | self.c.r[fC]
        self.c.r[rF] = (r[1] & 0xD0) | f
        self.c.r[rpHL] = word(hl + 1)
        self.c.r[rpBC] = bc
        if not disass:
            return
        return "CPI"

    def cpir(self, disass=False):
        bc = word(self.c.r[rpBC] - 1)
        hl = self.c.r[rpHL]
        r = sub8(self.c.r[rA], self.c.rdmem(hl), 0)
        t = r[0] - ((r[1] & 0x10) >> 4)
        f = 0x06 if bc else 0x02
        f |= (t & 0x08) | ((t & 0x02) << 4) | self.c.r[fC]
        self.c.r[rF] = (r[1] & 0xD0) | f
        self.c.r[rpHL] = word(hl + 1)
        self.c.r[rpBC] = bc
        if bc and (not (r[1] & 0x40)):
            self.c.r[rpPC] = word(self.c.r[rpPC] - 2)
        if not disass:
            return
        return "CPI"

    def cpd(self, disass=False):
        bc = word(self.c.r[rpBC] - 1)
        hl = self.c.r[rpHL]
        r = sub8(self.c.r[rA], self.c.rdmem(hl), 0)
        t = r[0] - ((r[1] & 0x10) >> 4)
        f = 0x06 if bc else 0x02
        f |= (t & 0x08) | ((t & 0x02) << 4) | self.c.r[fC]
        self.c.r[rF] = (r[1] & 0xD0) | f
        self.c.r[rpHL] = word(hl - 1)
        self.c.r[rpBC] = bc
        if not disass:
            return
        return "CPD"

    def cpdr(self, disass=False):
        bc = word(self.c.r[rpBC] - 1)
        hl = self.c.r[rpHL]
        r = sub8(self.c.r[rA], self.c.rdmem(hl), 0)
        t = r[0] - ((r[1] & 0x10) >> 4)
        f = 0x06 if bc else 0x02
        f |= (t & 0x08) | ((t & 0x02) << 4) | self.c.r[fC]
        self.c.r[rF] = (r[1] & 0xD0) | f
        self.c.r[rpHL] = word(hl - 1)
        self.c.r[rpBC] = bc
        if bc and (not (r[1] & 0x40)):
            self.c.r[rpPC] = word(self.c.r[rpPC] - 2)
        if not disass:
            return
        return "CPDR"

    def ini(self, disass=False):
        r = sub8(self.c.r[rB], 1, 0)
        hl = self.c.r[rpHL]
        self.c.wrmem(hl, self.c.rdinp(self.c.r[rpBC]))
        self.c.r[rpHL] = word(hl + 1)
        self.c.r[rB] = r[0]
        self.c.r[rF] = self.c.r[fC] | (r[1] & 0xFE)
        if not disass:
            return
        return "INI"

    def inir(self, disass=False):
        r = sub8(self.c.r[rB], 1, 0)
        hl = self.c.r[rpHL]
        self.c.wrmem(hl, self.c.rdinp(self.c.r[rpBC]))
        self.c.r[rpHL] = word(hl + 1)
        self.c.r[rB] = r[0]
        self.c.r[rF] = self.c.r[fC] | (r[1] & 0xFE)
        if not r[0]:
            self.c.r[rpPC] = word(self.c.r[rpPC] - 2)
        if not disass:
            return
        return "INIR"

    def ind(self, disass=False):
        r = sub8(self.c.r[rB], 1, 0)
        hl = self.c.r[rpHL]
        self.c.wrmem(hl, self.c.rdinp(self.c.r[rpBC]))
        self.c.r[rpHL] = word(hl - 1)
        self.c.r[rB] = r[0]
        self.c.r[rF] = self.c.r[fC] | (r[1] & 0xFE)
        if not disass:
            return
        return "IND"

    def indr(self, disass=False):
        r = sub8(self.c.r[rB], 1, 0)
        hl = self.c.r[rpHL]
        self.c.wrmem(hl, self.c.rdinp(self.c.r[rpBC]))
        self.c.r[rpHL] = word(hl + 1)
        self.c.r[rB] = r[0]
        self.c.r[rF] = self.c.r[fC] | (r[1] & 0xFE)
        if not r[0]:
            self.c.r[rpPC] = word(self.c.r[rpPC] - 2)
        if not disass:
            return
        return "INDR"

    def outi(self, disass=False):
        r = sub8(self.c.r[rB], 1, 0)
        hl = self.c.r[rpHL]
        self.c.wrout(self.c.r[rpBC], self.c.rdmem(hl))
        self.c.r[rpHL] = word(hl + 1)
        self.c.r[rB] = r[0]
        self.c.r[rF] = self.c.r[fC] | (r[1] & 0xFE)
        if not disass:
            return
        return "OUTI"

    def otir(self, disass=False):
        r = sub8(self.c.r[rB], 1, 0)
        hl = self.c.r[rpHL]
        self.c.wrout(self.c.r[rpBC], self.c.rdmem(hl))
        self.c.r[rpHL] = word(hl + 1)
        self.c.r[rB] = r[0]
        self.c.r[rF] = self.c.r[fC] | (r[1] & 0xFE)
        if not r[0]:
            self.c.r[rpPC] = word(self.c.r[rpPC] - 2)
        if not disass:
            return
        return "OTIR"

    def outd(self, disass=False):
        r = sub8(self.c.r[rB], 1, 0)
        hl = self.c.r[rpHL]
        self.c.wrout(self.c.r[rpBC], self.c.rdmem(hl))
        self.c.r[rpHL] = word(hl - 1)
        self.c.r[rB] = r[0]
        self.c.r[rF] = self.c.r[fC] | (r[1] & 0xFE)
        if not disass:
            return
        return "OUTD"

    def otdr(self, disass=False):
        r = sub8(self.c.r[rB], 1, 0)
        hl = self.c.r[rpHL]
        self.c.wrout(self.c.r[rpBC], self.c.rdmem(hl))
        self.c.r[rpHL] = word(hl - 1)
        self.c.r[rB] = r[0]
        self.c.r[rF] = self.c.r[fC] | (r[1] & 0xFE)
        if not r[0]:
            self.c.r[rpPC] = word(self.c.r[rpPC] - 2)
        if not disass:
            return
        return "OTDR"

    def getinstr(self):
        rv = {}

        # ldi, ldir, ldd, lddr
        # cpi, cpir, cpd, cpdr
        rv.update({bytes([0xED, 0xA0]): self.ldi})
        rv.update({bytes([0xED, 0xB0]): self.ldir})
        rv.update({bytes([0xED, 0xA8]): self.ldd})
        rv.update({bytes([0xED, 0xB8]): self.lddr})
        rv.update({bytes([0xED, 0xA1]): self.cpi})
        rv.update({bytes([0xED, 0xB1]): self.cpir})
        rv.update({bytes([0xED, 0xA9]): self.cpd})
        rv.update({bytes([0xED, 0xB9]): self.cpdr})

        # ini, inir, ind, indr
        # outi, otir, outd, otdr
        rv.update({bytes([0xED, 0xA2]): self.ini})
        rv.update({bytes([0xED, 0xB2]): self.inir})
        rv.update({bytes([0xED, 0xAA]): self.ind})
        rv.update({bytes([0xED, 0xBA]): self.indr})
        rv.update({bytes([0xED, 0xA3]): self.outi})
        rv.update({bytes([0xED, 0xB3]): self.otir})
        rv.update({bytes([0xED, 0xAB]): self.outd})
        rv.update({bytes([0xED, 0xBB]): self.otdr})

        return rv
