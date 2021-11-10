#
# Z80 arithmetic and logic instructions
#


from utils import *


class alu:

    def __init__(self, parent):
        self.c = parent

    def addai(self, disass=False):
        d = self.c.fetch()
        r = add8(self.c.r[rA], d, 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]        
        if not disass:
            return
        return "ADD A,{:02X}".format(d)

    def addar(self, disass=False):
        r1s = rname[self.c.r1]
        r = add8(self.c.r[rA], self.c.r[r1s], 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADD A,{:s}".format(rstr[r1s])

    def addax(self, disass=False):
        r1s = rxname[self.c.r1]
        r = add8(self.c.r[rA], self.c.r[r1s], 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADD A,{:s}".format(rstr[r1s])

    def adday(self, disass=False):
        r1s = ryname[self.c.r1]
        r = add8(self.c.r[rA], self.c.r[r1s], 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADD A,{:s}".format(rstr[r1s])

    def addam(self, disass=False):
        d = self.c.rdmem(self.c.r[rpHL])
        r = add8(self.c.r[rA], d, 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADD A,(HL)"

    def addamx(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIX], dsp))
        r = add8(self.c.r[rA], d, 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADD A,(IX+{:02X})".format(dsp)

    def addamy(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIY], dsp))
        r = add8(self.c.r[rA], d, 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADD A,(IY+{:02X})".format(dsp)

    def adcai(self, disass=False):
        d = self.c.fetch()
        r = add8(self.c.r[rA], d, self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADC A,{:02X}".format(d)

    def adcar(self, disass=False):
        r1s = rname[self.c.r1]
        r = add8(self.c.r[rA], self.c.r[r1s], self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADC A,{:s}".format(rstr[r1s])

    def adcax(self, disass=False):
        r1s = rxname[self.c.r1]
        r = add8(self.c.r[rA], self.c.r[r1s], self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADC A,{:s}".format(rstr[r1s])

    def adcay(self, disass=False):
        r1s = ryname[self.c.r1]
        r = add8(self.c.r[rA], self.c.r[r1s], self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADC A,{:s}".format(rstr[r1s])

    def adcam(self, disass=False):
        d = self.c.rdmem(self.c.r[rpHL])
        r = add8(self.c.r[rA], d, self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADC A,(HL)"

    def adcamx(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIX], dsp))
        r = add8(self.c.r[rA], d, self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADC A,(IX+{:02X})".format(dsp)

    def adcamy(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIY], dsp))
        r = add8(self.c.r[rA], d, self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADC A,(IY+{:02X})".format(dsp)

    def subai(self, disass=False):
        d = self.c.fetch()
        r = sub8(self.c.r[rA], d, 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SUB {:02X}".format(d)

    def subar(self, disass=False):
        r1s = rname[self.c.r1]
        r = sub8(self.c.r[rA], self.c.r[r1s], 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SUB {:s}".format(rstr[r1s])

    def subax(self, disass=False):
        r1s = rxname[self.c.r1]
        r = sub8(self.c.r[rA], self.c.r[r1s], 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SUB {:s}".format(rstr[r1s])

    def subay(self, disass=False):
        r1s = ryname[self.c.r1]
        r = sub8(self.c.r[rA], self.c.r[r1s], 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SUB {:s}".format(rstr[r1s])

    def subam(self, disass=False):
        d = self.c.rdmem(self.c.r[rpHL])
        r = sub8(self.c.r[rA], d, 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SUB (HL)"

    def subamx(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIX], dsp))
        r = sub8(self.c.r[rA], d, 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SUB (IX+{:02X})".format(dsp)

    def subamy(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIY], dsp))
        r = sub8(self.c.r[rA], d, 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SUB (IY+{:02X})".format(dsp)

    def sbcai(self, disass=False):
        d = self.c.fetch()
        r = sub8(self.c.r[rA], d, self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SBC {:02X}".format(d)

    def sbcar(self, disass=False):
        r1s = rname[self.c.r1]
        r = sub8(self.c.r[rA], self.c.r[r1s], self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SBC {:s}".format(rstr[r1s])

    def sbcax(self, disass=False):
        r1s = rxname[self.c.r1]
        r = sub8(self.c.r[rA], self.c.r[r1s], self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SBC {:s}".format(rstr[r1s])

    def sbcay(self, disass=False):
        r1s = ryname[self.c.r1]
        r = sub8(self.c.r[rA], self.c.r[r1s], self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SBC {:s}".format(rstr[r1s])

    def sbcam(self, disass=False):
        d = self.c.rdmem(self.c.r[rpHL])
        r = sub8(self.c.r[rA], d, self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SBC (HL)"

    def sbcamx(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIX], dsp))
        r = sub8(self.c.r[rA], d, self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SBC (IX+{:02X})".format(dsp)

    def sbcamy(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIY], dsp))
        r = sub8(self.c.r[rA], d, self.c.r[fC])
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SBC (IY+{:02X})".format(dsp)

    def andai(self, disass=False):
        d = self.c.fetch()
        r = lobyte(self.c.r[rA] & d)
        self.c.r[rA] = r
        self.c.r[rF] = logf(r) | 0x10
        if not disass:
            return
        return "AND {:02X}".format(d)

    def andar(self, disass=False):
        r1s = rname[self.c.r1]
        r = lobyte(self.c.r[rA] & self.c.r[r1s])
        self.c.r[rA] = r
        self.c.r[rF] = logf(r) | 0x10
        if not disass:
            return
        return "AND {:s}".format(rstr[r1s])

    def andax(self, disass=False):
        r1s = rxname[self.c.r1]
        r = lobyte(self.c.r[rA] & self.c.r[r1s])
        self.c.r[rA] = r
        self.c.r[rF] = logf(r) | 0x10
        if not disass:
            return
        return "AND {:s}".format(rstr[r1s])

    def anday(self, disass=False):
        r1s = ryname[self.c.r1]
        r = lobyte(self.c.r[rA] & self.c.r[r1s])
        self.c.r[rA] = r
        self.c.r[rF] = logf(r) | 0x10
        if not disass:
            return
        return "AND {:s}".format(rstr[r1s])

    def andam(self, disass=False):
        d = self.c.rdmem(self.c.r[rpHL])
        r = lobyte(self.c.r[rA] & d)
        self.c.r[rA] = r
        self.c.r[rF] = logf(r) | 0x10
        if not disass:
            return
        return "AND (HL)"

    def andamx(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIX], dsp))
        r = lobyte(self.c.r[rA] & d)
        self.c.r[rA] = r
        self.c.r[rF] = logf(r) | 0x10
        if not disass:
            return
        return "AND (IX+{:02X})".format(dsp)

    def andamy(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIY], dsp))
        r = lobyte(self.c.r[rA] & d)
        self.c.r[rA] = r
        self.c.r[rF] = logf(r) | 0x10
        if not disass:
            return
        return "AND IY+{:02X})".format(dsp)

    def orai(self, disass=False):
        d = self.c.fetch()
        r = lobyte(self.c.r[rA] | d)
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "OR {:02X}".format(d)

    def orar(self, disass=False):
        r1s = rname[self.c.r1]
        r = lobyte(self.c.r[rA] | self.c.r[r1s])
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "OR {:s}".format(rstr[r1s])

    def orax(self, disass=False):
        r1s = rxname[self.c.r1]
        r = lobyte(self.c.r[rA] | self.c.r[r1s])
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "OR {:s}".format(rstr[r1s])

    def oray(self, disass=False):
        r1s = ryname[self.c.r1]
        r = lobyte(self.c.r[rA] | self.c.r[r1s])
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "OR {:s}".format(rstr[r1s])

    def oram(self, disass=False):
        d = self.c.rdmem(self.c.r[rpHL])
        r = lobyte(self.c.r[rA] | d)
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "OR (HL)"

    def oramx(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIX], dsp))
        r = lobyte(self.c.r[rA] | d)
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "OR (IX+{:02X})".format(dsp)

    def oramy(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIY], dsp))
        r = lobyte(self.c.r[rA] | d)
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "OR (IY+{:02X})".format(dsp)

    def xorai(self, disass=False):
        d = self.c.fetch()
        r = lobyte(self.c.r[rA] ^ d)
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "XOR {:02X}".format(d)

    def xorar(self, disass=False):
        r1s = rname[self.c.r1]
        r = lobyte(self.c.r[rA] ^ self.c.r[r1s])
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "XOR {:s}".format(rstr[r1s])

    def xorax(self, disass=False):
        r1s = rxname[self.c.r1]
        r = lobyte(self.c.r[rA] ^ self.c.r[r1s])
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "XOR {:s}".format(rstr[r1s])

    def xoray(self, disass=False):
        r1s = ryname[self.c.r1]
        r = lobyte(self.c.r[rA] ^ self.c.r[r1s])
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "XOR {:s}".format(rstr[r1s])

    def xoram(self, disass=False):
        d = self.c.rdmem(self.c.r[rpHL])
        r = lobyte(self.c.r[rA] ^ d)
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "XOR (HL)"

    def xoramx(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIX], dsp))
        r = lobyte(self.c.r[rA] ^ d)
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "XOR (IX+{:02X})".format(dsp)

    def xoramy(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIY], dsp))
        r = lobyte(self.c.r[rA] ^ d)
        self.c.r[rA] = r
        self.c.r[rF] = logf(r)
        if not disass:
            return
        return "XOR (IY+{:02X})".format(dsp)

    def cpai(self, disass=False):
        d = self.c.fetch()
        r = sub8(self.c.r[rA], d, 0)
        self.c.r[rF] = (r[1] & 0xD7) | (d & 0x28)
        if not disass:
            return
        return "CP {:02X}".format(d)

    def cpar(self, disass=False):
        r1s = rname[self.c.r1]
        d = self.c.r[r1s]
        r = sub8(self.c.r[rA], d, 0)
        self.c.r[rF] = (r[1] & 0xD7) | (d & 0x28)
        if not disass:
            return
        return "CP {:s}".format(rstr[r1s])

    def cpax(self, disass=False):
        r1s = rxname[self.c.r1]
        d = self.c.r[r1s]
        r = sub8(self.c.r[rA], d, 0)
        self.c.r[rF] = (r[1] & 0xD7) | (d & 0x28)
        if not disass:
            return
        return "CP {:s}".format(rstr[r1s])

    def cpay(self, disass=False):
        r1s = ryname[self.c.r1]
        d = self.c.r[r1s]
        r = sub8(self.c.r[rA], d, 0)
        self.c.r[rF] = (r[1] & 0xD7) | (d & 0x28)
        if not disass:
            return
        return "CP {:s}".format(rstr[r1s])

    def cpam(self, disass=False):
        d = self.c.rdmem(self.c.r[rpHL])
        r = sub8(self.c.r[rA], d, 0)
        self.c.r[rF] = (r[1] & 0xD7) | (d & 0x28)
        if not disass:
            return
        return "CP (HL)"

    def cpamx(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIX], dsp))
        r = sub8(self.c.r[rA], d, 0)
        self.c.r[rF] = (r[1] & 0xD7) | (d & 0x28)
        if not disass:
            return
        return "CP (IX+{:02X})".format(dsp)

    def cpamy(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.rdmem(adddsp(self.c.r[rpIY], dsp))
        r = sub8(self.c.r[rA], d, 0)
        self.c.r[rF] = (r[1] & 0xD7) | (d & 0x28)
        if not disass:
            return
        return "CP (IY+{:02X})".format(dsp)

    def addrp(self, disass=False):
        rps = rpname[self.c.rp]
        r = add16(self.c.r[rpHL], self.c.r[rps], 0)
        f = self.c.r[rF] & 0xC4
        self.c.r[rpHL] = r[0]
        self.c.r[rF] = f | (r[1] & 0x39)
        if not disass:
            return
        return "ADD HL,{:s}".format(rstr[rps])

    def addrpx(self, disass=False):
        rps = rpxname[self.c.rp]
        r = add16(self.c.r[rpIX], self.c.r[rps], 0)
        f = self.c.r[rF] & 0xC4
        self.c.r[rpIX] = r[0]
        self.c.r[rF] = f | (r[1] & 0x39)
        if not disass:
            return
        return "ADD IX,{:s}".format(rstr[rps])

    def addrpy(self, disass=False):
        rps = rpyname[self.c.rp]
        r = add16(self.c.r[rpIY], self.c.r[rps], 0)
        f = self.c.r[rF] & 0xC4
        self.c.r[rpIY] = r[0]
        self.c.r[rF] = f | (r[1] & 0x39)
        if not disass:
            return
        return "ADD IY,{:s}".format(rstr[rps])

    def adcrp(self, disass=False):
        rps = rpname[self.c.rp]
        r = add16(self.c.r[rpHL], self.c.r[rps], self.c.r[fC])
        self.c.r[rpHL] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "ADC HL,{:s}".format(rstr[rps])

    def sbcrp(self, disass=False):
        rps = rpname[self.c.rp]
        r = sub16(self.c.r[rpHL], self.c.r[rps], self.c.r[fC])
        self.c.r[rpHL] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "SBC HL,{:s}".format(rstr[rps])

    def daa(self, disass=False):
        c = 0
        d = self.c.r[rA]
        n = self.c.r[fN]
        if n:
            if self.c.r[fC]:
                d -= 0x60
            if self.c.r[fH]:
                d -= 0x06
        else:
            if self.c.r[fC] or (d > 0x99):
                d += 0x60
                c = 1
            if self.c.r[fH] or ((d & 0x0F) > 0x09):
                d += 0x06

        self.c.r[rA] = d
        self.c.r[rF] = (logf(d) & 0xEC) | c | (n << 1)
        if not disass:
            return
        return "DAA"

    def cpla(self, disass=False):
        d = self.c.r[rA]
        f = (self.c.r[rF] & 0xC5) | 0x12
        f |= (d & 0x28)
        self.c.r[rA] = lobyte(~d)
        self.c.r[rF] = f
        if not disass:
            return
        return "CPL"

    def nega(self, disass=False):
        r = sub8(0, self.c.r[rA], 0)
        self.c.r[rA] = r[0]
        self.c.r[rF] = r[1]
        if not disass:
            return
        return "NEG"

    def rla(self, disass=False):
        d = self.c.r[rA]
        f = self.c.r[rF]
        c = 1 if d & 0x80 else 0
        d = lobyte(d << 1) | (f & 1)
        self.c.r[rA] = d
        self.c.r[rF] = (f & 0xC4) | (d & 0x28) | c
        if not disass:
            return
        return "RLA"

    def rra(self, disass=False):
        d = self.c.r[rA]
        f = self.c.r[rF]
        c = 1 if d & 0x01 else 0
        d = lobyte(d >> 1) | ((f & 1) << 7)
        self.c.r[rA] = d
        self.c.r[rF] = (f & 0xC4) | (d & 0x28) | c
        if not disass:
            return
        return "RRA"

    def rlca(self, disass=False):
        d = self.c.r[rA]
        f = self.c.r[rF]
        c = 1 if d & 0x80 else 0
        d = lobyte(d << 1) | c
        self.c.r[rA] = d
        self.c.r[rF] = (f & 0xC4) | (d & 0x28) | c
        if not disass:
            return
        return "RLCA"

    def rrca(self, disass=False):
        d = self.c.r[rA]
        f = self.c.r[rF]
        c = 1 if d & 0x01 else 0
        d = lobyte(d >> 1) | (c << 7)
        self.c.r[rA] = d
        self.c.r[rF] = (f & 0xC4) | (d & 0x28) | c
        if not disass:
            return
        return "RRCA"

    def rrd(self, disass=False):
        hl = self.c.r[rpHL]
        a = self.c.r[rA]
        f = self.c.r[rF]
        d = self.c.rdmem(hl)
        self.c.wrmem(hl, lobyte((d >> 4) | (a << 4)))
        r = (a & 0xF0) | (d & 0x0F)
        self.c.r[rA] = r
        self.c.r[rF] = (f & 1) | (logf(r) & 0xFE)
        if not disass:
            return
        return "RRD"

    def rld(self, disass=False):
        hl = self.c.r[rpHL]
        a = self.c.r[rA]
        f = self.c.r[rF]
        d = self.c.rdmem(hl)
        self.c.wrmem(hl, lobyte((d << 4) | (a & 0x0F)))
        r = (a & 0xF0) | ((d >> 4) & 0x0F)
        self.c.r[rA] = r
        self.c.r[rF] = (f & 1) | (logf(r) & 0xFE)
        if not disass:
            return
        return "RLD"

    def getinstr(self):
        rv = {}

        # addai, adcai, subai, sbcai
        rv.update({b'\xC6': self.addai})
        rv.update({b'\xdd\xC6': self.addai})
        rv.update({b'\xfd\xC6': self.addai})
        rv.update({b'\xCE': self.adcai})
        rv.update({b'\xdd\xCE': self.adcai})
        rv.update({b'\xfd\xCE': self.adcai})
        rv.update({b'\xD6': self.subai})
        rv.update({b'\xdd\xD6': self.subai})
        rv.update({b'\xfd\xD6': self.subai})
        rv.update({b'\xDE': self.sbcai})
        rv.update({b'\xdd\xDE': self.sbcai})
        rv.update({b'\xfd\xDE': self.sbcai})

        # andai, xorai, orai, cpai
        rv.update({b'\xE6': self.andai})
        rv.update({b'\xdd\xE6': self.andai})
        rv.update({b'\xfd\xE6': self.andai})
        rv.update({b'\xEE': self.xorai})
        rv.update({b'\xdd\xEE': self.xorai})
        rv.update({b'\xfd\xEE': self.xorai})
        rv.update({b'\xF6': self.orai})
        rv.update({b'\xdd\xF6': self.orai})
        rv.update({b'\xfd\xF6': self.orai})
        rv.update({b'\xFE': self.cpai})
        rv.update({b'\xdd\xFE': self.cpai})
        rv.update({b'\xfd\xFE': self.cpai})

        # addar, adcar, subar, sbcar
        for r1 in [0, 1, 2, 3, 4, 5, 7]:
            rv.update({bytes([0x80 | r1]): self.addar})
            rv.update({bytes([0xdd, 0x80 | r1]): self.addax})
            rv.update({bytes([0xfd, 0x80 | r1]): self.adday})
            rv.update({bytes([0x88 | r1]): self.adcar})
            rv.update({bytes([0xdd, 0x88 | r1]): self.adcax})
            rv.update({bytes([0xfd, 0x88 | r1]): self.adcay})
            rv.update({bytes([0x90 | r1]): self.subar})
            rv.update({bytes([0xdd, 0x90 | r1]): self.subax})
            rv.update({bytes([0xfd, 0x90 | r1]): self.subay})
            rv.update({bytes([0x98 | r1]): self.sbcar})
            rv.update({bytes([0xdd, 0x98 | r1]): self.sbcax})
            rv.update({bytes([0xfd, 0x98 | r1]): self.sbcay})

        # andar, xorar, orar, cpar
        for r1 in [0, 1, 2, 3, 4, 5, 7]:
            rv.update({bytes([0xA0 | r1]): self.andar})
            rv.update({bytes([0xdd, 0xA0 | r1]): self.andax})
            rv.update({bytes([0xfd, 0xA0 | r1]): self.anday})
            rv.update({bytes([0xA8 | r1]): self.xorar})
            rv.update({bytes([0xdd, 0xA8 | r1]): self.xorax})
            rv.update({bytes([0xfd, 0xA8 | r1]): self.xoray})
            rv.update({bytes([0xB0 | r1]): self.orar})
            rv.update({bytes([0xdd, 0xB0 | r1]): self.orax})
            rv.update({bytes([0xfd, 0xB0 | r1]): self.oray})
            rv.update({bytes([0xB8 | r1]): self.cpar})
            rv.update({bytes([0xdd, 0xB8 | r1]): self.cpax})
            rv.update({bytes([0xfd, 0xB8 | r1]): self.cpay})

        # addam, addamx, addamy, adcam, adcamx, adcamy
        # subam, subamx, subamy, sbcam, sbcamx, sbcamy
        rv.update({b'\x86': self.addam})
        rv.update({b'\xdd\x86': self.addamx})
        rv.update({b'\xfd\x86': self.addamy})
        rv.update({b'\x8E': self.adcam})
        rv.update({b'\xdd\x8E': self.adcamx})
        rv.update({b'\xfd\x8E': self.adcamy})
        rv.update({b'\x96': self.subam})
        rv.update({b'\xdd\x96': self.subamx})
        rv.update({b'\xfd\x96': self.subamy})
        rv.update({b'\x9E': self.sbcam})
        rv.update({b'\xdd\x9E': self.sbcamx})
        rv.update({b'\xfd\x9E': self.sbcamy})

        # andam, andamx, andamy, xoram, xoramx, xoramy
        # oram, oramx, oramy, cpam, cpamx, cpamy
        rv.update({b'\xA6': self.andam})
        rv.update({b'\xdd\xA6': self.andamx})
        rv.update({b'\xfd\xA6': self.andamy})
        rv.update({b'\xAE': self.xoram})
        rv.update({b'\xdd\xAE': self.xoramx})
        rv.update({b'\xfd\xAE': self.xoramy})
        rv.update({b'\xB6': self.oram})
        rv.update({b'\xdd\xB6': self.oramx})
        rv.update({b'\xfd\xB6': self.oramy})
        rv.update({b'\xBE': self.cpam})
        rv.update({b'\xdd\xBE': self.cpamx})
        rv.update({b'\xfd\xBE': self.cpamy})

        # addrp, addrpx, addrpy, adcrp, sbcrp
        # nega
        for rp in range(4):
            rv.update({bytes([0x09 | (rp << 4)]): self.addrp})
            rv.update({bytes([0xDD, 0x09 | (rp << 4)]): self.addrpx})
            rv.update({bytes([0xFD, 0x09 | (rp << 4)]): self.addrpy})
            rv.update({bytes([0xED, 0x4A | (rp << 4)]): self.adcrp})
            rv.update({bytes([0xED, 0x42 | (rp << 4)]): self.sbcrp})
            rv.update({bytes([0xED, 0x44 | (rp << 4)]): self.nega})
            rv.update({bytes([0xED, 0x4C | (rp << 4)]): self.nega})

        # daa, cpla, rla, rra, rlca, rrca
        rv.update({b'\x27': self.daa})
        rv.update({b'\xdd\x27': self.daa})
        rv.update({b'\xfd\x27': self.daa})
        rv.update({b'\x2f': self.cpla})
        rv.update({b'\xdd\x2f': self.cpla})
        rv.update({b'\xfd\x2f': self.cpla})
        rv.update({b'\x17': self.rla})
        rv.update({b'\xdd\x17': self.rla})
        rv.update({b'\xfd\x17': self.rla})
        rv.update({b'\x07': self.rlca})
        rv.update({b'\xdd\x07': self.rlca})
        rv.update({b'\xfd\x07': self.rlca})
        rv.update({b'\x1f': self.rra})
        rv.update({b'\xdd\x1f': self.rra})
        rv.update({b'\xfd\x1f': self.rra})
        rv.update({b'\x0f': self.rrca})
        rv.update({b'\xdd\x0f': self.rrca})
        rv.update({b'\xfd\x0f': self.rrca})

        # rrd, rld
        rv.update({b'\xed\x67': self.rrd})
        rv.update({b'\xed\x6f': self.rld})

        return rv
