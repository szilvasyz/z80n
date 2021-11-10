#
# Z80 pushes, pops, calls, rets
#


from utils import *


class stack:

    def __init__(self, parent):
        self.c = parent

    def push(self, disass=False):
        rps = rp2name[self.c.rp]
        self.c.push(self.c.r[rps])
        if not disass:
            return
        return "PUSH {:s}".format(rstr[rps])

    def pushx(self, disass=False):
        rps = rp2xname[self.c.rp]
        self.c.push(self.c.r[rps])
        if not disass:
            return
        return "PUSH {:s}".format(rstr[rps])

    def pushy(self, disass=False):
        rps = rp2yname[self.c.rp]
        self.c.push(self.c.r[rps])
        if not disass:
            return
        return "PUSH {:s}".format(rstr[rps])

    def pop(self, disass=False):
        rps = rp2name[self.c.rp]
        self.c.r[rps] = self.c.pop()
        if not disass:
            return
        return "POP {:s}".format(rstr[rps])

    def popx(self, disass=False):
        rps = rp2xname[self.c.rp]
        self.c.r[rps] = self.c.pop()
        if not disass:
            return
        return "POP {:s}".format(rstr[rps])

    def popy(self, disass=False):
        rps = rp2yname[self.c.rp]
        self.c.r[rps] = self.c.pop()
        if not disass:
            return
        return "POP {:s}".format(rstr[rps])

    def call(self, disass=False):
        a = self.c.fetch16()
        self.c.push(self.c.r[rpPC])
        self.c.r[rpPC] = a
        if not disass:
            return
        return "CALL {:04X}".format(a)

    def ret(self, disass=False):
        a = self.c.pop()
        self.c.r[rpPC] = a
        if not disass:
            return
        return "RET"

    def reti(self, disass=False):
        a = self.c.pop()
        self.c.r[rpPC] = a
        if not disass:
            return
        return "RETI"

    def retn(self, disass=False):
        a = self.c.pop()
        self.c.r[rpPC] = a
        self.c.iff1 = self.c.iff2
        if not disass:
            return
        return "RETN"

    def callnz(self, disass=False):
        a = self.c.fetch16()
        if not self.c.r[fZ]:
            self.c.push(self.c.r[rpPC])
            self.c.r[rpPC] = a
        if not disass:
            return
        return "CALL NZ,{:04X}".format(a)

    def callz(self, disass=False):
        a = self.c.fetch16()
        if self.c.r[fZ]:
            self.c.push(self.c.r[rpPC])
            self.c.r[rpPC] = a
        if not disass:
            return
        return "CALL Z,{:04X}".format(a)

    def callnc(self, disass=False):
        a = self.c.fetch16()
        if not self.c.r[fC]:
            self.c.push(self.c.r[rpPC])
            self.c.r[rpPC] = a
        if not disass:
            return
        return "CALL NC,{:04X}".format(a)

    def callc(self, disass=False):
        a = self.c.fetch16()
        if self.c.r[fC]:
            self.c.push(self.c.r[rpPC])
            self.c.r[rpPC] = a
        if not disass:
            return
        return "CALL C,{:04X}".format(a)

    def callpo(self, disass=False):
        a = self.c.fetch16()
        if not self.c.r[fP]:
            self.c.push(self.c.r[rpPC])
            self.c.r[rpPC] = a
        if not disass:
            return
        return "CALL PO,{:04X}".format(a)

    def callpe(self, disass=False):
        a = self.c.fetch16()
        if self.c.r[fP]:
            self.c.push(self.c.r[rpPC])
            self.c.r[rpPC] = a
        if not disass:
            return
        return "CALL PE,{:04X}".format(a)

    def callp(self, disass=False):
        a = self.c.fetch16()
        if not self.c.r[fS]:
            self.c.push(self.c.r[rpPC])
            self.c.r[rpPC] = a
        if not disass:
            return
        return "CALL P,{:04X}".format(a)

    def callm(self, disass=False):
        a = self.c.fetch16()
        if self.c.r[fS]:
            self.c.push(self.c.r[rpPC])
            self.c.r[rpPC] = a
        if not disass:
            return
        return "CALL M,{:04X}".format(a)

    def retnz(self, disass=False):
        if not self.c.r[fZ]:
            a = self.c.pop()
            self.c.r[rpPC] = a
        if not disass:
            return
        return "RET NZ"

    def retz(self, disass=False):
        if self.c.r[fZ]:
            a = self.c.pop()
            self.c.r[rpPC] = a
        if not disass:
            return
        return "RET Z"

    def retnc(self, disass=False):
        if not self.c.r[fC]:
            a = self.c.pop()
            self.c.r[rpPC] = a
        if not disass:
            return
        return "RET NC"

    def retc(self, disass=False):
        if self.c.r[fC]:
            a = self.c.pop()
            self.c.r[rpPC] = a
        if not disass:
            return
        return "RET C"

    def retpo(self, disass=False):
        if not self.c.r[fP]:
            a = self.c.pop()
            self.c.r[rpPC] = a
        if not disass:
            return
        return "RET PO"

    def retpe(self, disass=False):
        if self.c.r[fP]:
            a = self.c.pop()
            self.c.r[rpPC] = a
        if not disass:
            return
        return "RET PE"

    def retp(self, disass=False):
        if not self.c.r[fS]:
            a = self.c.pop()
            self.c.r[rpPC] = a
        if not disass:
            return
        return "RET P"

    def retm(self, disass=False):
        if self.c.r[fS]:
            a = self.c.pop()
            self.c.r[rpPC] = a
        if not disass:
            return
        return "RET M"

    def rst(self, disass=False):
        a = self.c.r0 << 3
        self.c.push(self.c.r[rpPC])
        self.c.r[rpPC] = a
        if not disass:
            return
        return "RST {:02X}".format(a)

    def getinstr(self):
        rv = {}
        for rp in range(4):
            rv.update({
                bytes([0xC5 | (rp << 4)]): self.push,
                bytes([0xDD, 0xC5 | (rp << 4)]): self.push,
                bytes([0xFD, 0xC5 | (rp << 4)]): self.push,
                bytes([0xC1 | (rp << 4)]): self.pop,
                bytes([0xDD, 0xC1 | (rp << 4)]): self.pop,
                bytes([0xFD, 0xC1 | (rp << 4)]): self.pop
            })

        rv.update({b'\xdd\xe5': self.pushx})
        rv.update({b'\xdd\xe1': self.popx})

        rv.update({b'\xfd\xe5': self.pushy})
        rv.update({b'\xfd\xe1': self.popy})

        rv.update({b'\xcd': self.call})
        rv.update({b'\xdd\xcd': self.call})
        rv.update({b'\xfd\xcd': self.call})
        rv.update({b'\xc9': self.ret})
        rv.update({b'\xdd\xc9': self.ret})
        rv.update({b'\xfd\xc9': self.ret})

        rv.update({b'\xc4': self.callnz})
        rv.update({b'\xdd\xc4': self.callnz})
        rv.update({b'\xfd\xc4': self.callnz})
        rv.update({b'\xcc': self.callz})
        rv.update({b'\xdd\xcc': self.callz})
        rv.update({b'\xfd\xcc': self.callz})

        rv.update({b'\xd4': self.callnc})
        rv.update({b'\xdd\xd4': self.callnc})
        rv.update({b'\xfd\xd4': self.callnc})
        rv.update({b'\xdc': self.callc})
        rv.update({b'\xdd\xdc': self.callc})
        rv.update({b'\xfd\xdc': self.callc})

        rv.update({b'\xe4': self.callpo})
        rv.update({b'\xdd\xe4': self.callpo})
        rv.update({b'\xfd\xe4': self.callpo})
        rv.update({b'\xec': self.callpe})
        rv.update({b'\xdd\xec': self.callpe})
        rv.update({b'\xfd\xec': self.callpe})

        rv.update({b'\xf4': self.callp})
        rv.update({b'\xdd\xf4': self.callp})
        rv.update({b'\xfd\xf4': self.callp})
        rv.update({b'\xfc': self.callm})
        rv.update({b'\xdd\xfc': self.callm})
        rv.update({b'\xfd\xfc': self.callm})

        rv.update({b'\xc0': self.retnz})
        rv.update({b'\xdd\xc0': self.retnz})
        rv.update({b'\xfd\xc0': self.retnz})
        rv.update({b'\xc8': self.retz})
        rv.update({b'\xdd\xc8': self.retz})
        rv.update({b'\xfd\xc8': self.retz})

        rv.update({b'\xd0': self.retnc})
        rv.update({b'\xdd\xd0': self.retnc})
        rv.update({b'\xfd\xd0': self.retnc})
        rv.update({b'\xd8': self.retc})
        rv.update({b'\xdd\xd8': self.retc})
        rv.update({b'\xfd\xd8': self.retc})

        rv.update({b'\xe0': self.retpo})
        rv.update({b'\xdd\xe0': self.retpo})
        rv.update({b'\xfd\xe0': self.retpo})
        rv.update({b'\xe8': self.retpe})
        rv.update({b'\xdd\xe8': self.retpe})
        rv.update({b'\xfd\xe8': self.retpe})

        rv.update({b'\xf0': self.retp})
        rv.update({b'\xdd\xf0': self.retp})
        rv.update({b'\xfd\xf0': self.retp})
        rv.update({b'\xf8': self.retm})
        rv.update({b'\xdd\xf8': self.retm})
        rv.update({b'\xfd\xf8': self.retm})

        for r0 in range(8):
            rv.update({bytes([0xC7 | (r0 << 3)]): self.rst})
            rv.update({bytes([0xDD, 0xC7 | (r0 << 3)]): self.rst})
            rv.update({bytes([0xFD, 0xC7 | (r0 << 3)]): self.rst})
            rv.update({bytes([0xED, 0x45 | (r0 << 3)]): self.retn})

        rv.update({b'\xED\x4D': self.reti})

        return rv

