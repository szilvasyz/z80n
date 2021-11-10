#
# Z80 increments/decrements
#


from utils import *


class incdec:

    def __init__(self, parent):
        self.c = parent

    def incr(self, disass=False):
        r0s = rname[self.c.r0]
        f = self.c.r[rF] & 1
        r = add8(self.c.r[r0s], 1, 0)
        self.c.r[r0s] = r[0]
        self.c.r[rF] = f | (r[1] & 0xFE)
        if not disass:
            return
        return "INC {:s}".format(rstr[r0s])

    def incrx(self, disass=False):
        r0s = rxname[self.c.r0]
        f = self.c.r[rF] & 1
        r = add8(self.c.r[r0s], 1, 0)
        self.c.r[r0s] = r[0]
        self.c.r[rF] = f | (r[1] & 0xFE)
        if not disass:
            return
        return "INC {:s}".format(rstr[r0s])

    def incry(self, disass=False):
        r0s = ryname[self.c.r0]
        f = self.c.r[rF] & 1
        r = add8(self.c.r[r0s], 1, 0)
        self.c.r[r0s] = r[0]
        self.c.r[rF] = f | (r[1] & 0xFE)
        if not disass:
            return
        return "INC {:s}".format(rstr[r0s])

    def incm(self, disass=False):
        a = self.c.r[rpHL]
        f = self.c.r[rF] & 1
        r = add8(self.c.rdmem(a), 1, 0)
        self.c.wrmem(a, r[0])
        self.c.r[rF] = f | (r[1] & 0xFE)
        if not disass:
            return
        return "INC (HL)"

    def incmx(self, disass=False):
        dsp = self.c.fetch()
        a = adddsp(self.c.r[rpIX], dsp)
        f = self.c.r[rF] & 1
        r = add8(self.c.rdmem(a), 1, 0)
        self.c.wrmem(a, r[0])
        self.c.r[rF] = f | (r[1] & 0xFE)
        if not disass:
            return
        return "INC (IX+{:02X})".format(dsp)

    def incmy(self, disass=False):
        dsp = self.c.fetch()
        a = adddsp(self.c.r[rpIY], dsp)
        f = self.c.r[rF] & 1
        r = add8(self.c.rdmem(a), 1, 0)
        self.c.wrmem(a, r[0])
        self.c.r[rF] = f | (r[1] & 0xFE)
        if not disass:
            return
        return "INC (IY+{:02X})".format(dsp)

    def decr(self, disass=False):
        r0s = rname[self.c.r0]
        f = self.c.r[rF] & 1
        r = sub8(self.c.r[r0s], 1, 0)
        self.c.r[r0s] = r[0]
        self.c.r[rF] = f | (r[1] & 0xFE)
        if not disass:
            return
        return "DEC {:s}".format(rstr[r0s])

    def decrx(self, disass=False):
        r0s = rxname[self.c.r0]
        f = self.c.r[rF] & 1
        r = sub8(self.c.r[r0s], 1, 0)
        self.c.r[r0s] = r[0]
        self.c.r[rF] = f | (r[1] & 0xFE)
        if not disass:
            return
        return "DEC {:s}".format(rstr[r0s])

    def decry(self, disass=False):
        r0s = ryname[self.c.r0]
        f = self.c.r[rF] & 1
        r = sub8(self.c.r[r0s], 1, 0)
        self.c.r[r0s] = r[0]
        self.c.r[rF] = f | (r[1] & 0xFE)
        if not disass:
            return
        return "DEC {:s}".format(rstr[r0s])

    def decm(self, disass=False):
        a = self.c.r[rpHL]
        f = self.c.r[rF] & 1
        r = sub8(self.c.rdmem(a), 1, 0)
        self.c.wrmem(a, r[0])
        self.c.r[rF] = f | (r[1] & 0xFE)
        if not disass:
            return
        return "DEC (HL)"

    def decmx(self, disass=False):
        dsp = self.c.fetch()
        a = adddsp(self.c.r[rpIX], dsp)
        f = self.c.r[rF] & 1
        r = sub8(self.c.rdmem(a), 1, 0)
        self.c.wrmem(a, r[0])
        self.c.r[rF] = f | (r[1] & 0xFE)
        if not disass:
            return
        return "DEC (IX+{:02X})".format(dsp)

    def decmy(self, disass=False):
        dsp = self.c.fetch()
        a = adddsp(self.c.r[rpIY], dsp)
        f = self.c.r[rF] & 1
        r = sub8(self.c.rdmem(a), 1, 0)
        self.c.wrmem(a, r[0])
        self.c.r[rF] = f | (r[1] & 0xFE)
        if not disass:
            return
        return "DEC (IY+{:02X})".format(dsp)

    def incrp(self, disass=False):
        rp = rpname[self.c.rp]
        d = word(self.c.r[rp] + 1)
        self.c.r[rp] = d
        if not disass:
            return
        return "INC {:s}".format(rstr[rp])

    def incrpx(self, disass=False):
        rp = rpxname[self.c.rp]
        d = word(self.c.r[rp] + 1)
        self.c.r[rp] = d
        if not disass:
            return
        return "INC {:s}".format(rstr[rp])

    def incrpy(self, disass=False):
        rp = rpyname[self.c.rp]
        d = word(self.c.r[rp] + 1)
        self.c.r[rp] = d
        if not disass:
            return
        return "INC {:s}".format(rstr[rp])

    def decrp(self, disass=False):
        rp = rpname[self.c.rp]
        d = word(self.c.r[rp] - 1)
        self.c.r[rp] = d
        if not disass:
            return
        return "DEC {:s}".format(rstr[rp])

    def decrpx(self, disass=False):
        rp = rpxname[self.c.rp]
        d = word(self.c.r[rp] - 1)
        self.c.r[rp] = d
        if not disass:
            return
        return "DEC{:s}".format(rstr[rp])

    def decrpy(self, disass=False):
        rp = rpyname[self.c.rp]
        d = word(self.c.r[rp] - 1)
        self.c.r[rp] = d
        if not disass:
            return
        return "DEC{:s}".format(rstr[rp])

    def getinstr(self, disass=False):
        rv = {}

        # incr, incrx, incry, decr, decrx, decry
        for r1 in [0, 1, 2, 3, 4, 5, 7]:
            rv.update({bytes([0x04 | (r1 << 3)]): self.incr})
            rv.update({bytes([0xDD, 0x04 | (r1 << 3)]): self.incrx})
            rv.update({bytes([0xFD, 0x04 | (r1 << 3)]): self.incry})
            rv.update({bytes([0x05 | (r1 << 3)]): self.decr})
            rv.update({bytes([0xDD, 0x05 | (r1 << 3)]): self.decrx})
            rv.update({bytes([0xFD, 0x05 | (r1 << 3)]): self.decry})

        # incm, incmx, decm, decmx
        rv.update({b'\x34': self.incm})
        rv.update({b'\xdd\x34': self.incmx})
        rv.update({b'\xfd\x34': self.incmy})
        rv.update({b'\x35': self.decm})
        rv.update({b'\xdd\x35': self.decmx})
        rv.update({b'\xfd\x35': self.decmy})

        # incrp, incrpx, incrpy
        # decrp, decrpx, decrpy
        for rp in range(4):
            rv.update({bytes([0x03 | (rp << 4)]): self.incrp})
            rv.update({bytes([0xDD, 0x03 | (rp << 4)]): self.incrpx})
            rv.update({bytes([0xFD, 0x03 | (rp << 4)]): self.incrpy})
            rv.update({bytes([0x0B | (rp << 4)]): self.decrp})
            rv.update({bytes([0xDD, 0x0B | (rp << 4)]): self.decrpx})
            rv.update({bytes([0xFD, 0x0B | (rp << 4)]): self.decrpy})

        return rv
