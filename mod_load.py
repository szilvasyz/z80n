#
# Z80 load and exchange instructions
#


from utils import *


class load:

    def __init__(self, parent):
        self.c = parent

    def loadrr(self, disass=False):
        r0s = rname[self.c.r0]
        r1s = rname[self.c.r1]
        self.c.r[r0s] = self.c.r[r1s]
        if not disass:
            return
        return "LD {:s},{:s}".format(rstr[r0s], rstr[r1s])

    def loadxx(self, disass=False):
        r0s = rxname[self.c.r0]
        r1s = rxname[self.c.r1]
        self.c.r[r0s] = self.c.r[r1s]
        if not disass:
            return
        return "LD {:s},{:s}".format(rstr[r0s], rstr[r1s])

    def loadyy(self, disass=False):
        r0s = ryname[self.c.r0]
        r1s = ryname[self.c.r1]
        self.c.r[r0s] = self.c.r[r1s]
        if not disass:
            return
        return "LD {:s},{:s}".format(rstr[r0s], rstr[r1s])

    def loadrm(self, disass=False):
        r0s = rname[self.c.r0]
        d = self.c.rdmem(self.c.r[rpHL])
        self.c.r[r0s] = d
        if not disass:
            return
        return "LD {:s},(HL)".format(rstr[r0s])

    def loadmr(self, disass=False):
        r1s = rname[self.c.r1]
        d = self.c.r[r1s]
        self.c.wrmem(self.c.r[rpHL], d)
        if not disass:
            return
        return "LD (HL),{:s}".format(rstr[r1s])

    def loadrxm(self, disass=False):
        dsp = self.c.fetch()
        r0s = rname[self.c.r0]
        d = self.c.rdmem(adddsp(self.c.r[rpIX], dsp))
        self.c.r[r0s] = d
        if not disass:
            return
        return "LD {:s},(IX+{:02x})".format(rstr[r0s], dsp)

    def loadxmr(self, disass=False):
        dsp = self.c.fetch()
        r1s = rname[self.c.r1]
        d = self.c.r[r1s]
        self.c.wrmem(adddsp(self.c.r[rpIX], dsp), d)
        if not disass:
            return
        return "LD (IX+{:02x}),{:s}".format(dsp, rstr[r1s])

    def loadrym(self, disass=False):
        dsp = self.c.fetch()
        r0s = rname[self.c.r0]
        d = self.c.rdmem(adddsp(self.c.r[rpIY], dsp))
        self.c.r[r0s] = d
        if not disass:
            return
        return "LD {:s},(IY+{:02x})".format(rstr[r0s], dsp)

    def loadymr(self, disass=False):
        dsp = self.c.fetch()
        r1s = rname[self.c.r1]
        d = self.c.r[r1s]
        self.c.wrmem(adddsp(self.c.r[rpIY], dsp), d)
        if not disass:
            return
        return "LD (IY+{:02x}),{:s}".format(dsp, rstr[r1s])

    def loadri(self, disass=False):
        d = self.c.fetch()
        r0s = rname[self.c.r0]
        self.c.r[r0s] = d
        if not disass:
            return
        return "LD {:s},{:02X}".format(rstr[r0s], d)

    def loadrxi(self, disass=False):
        d = self.c.fetch()
        r0s = rxname[self.c.r0]
        self.c.r[r0s] = d
        if not disass:
            return
        return "LD {:s},{:02X}".format(rstr[r0s], d)

    def loadryi(self, disass=False):
        d = self.c.fetch()
        r0s = ryname[self.c.r0]
        self.c.r[r0s] = d
        if not disass:
            return
        return "LD {:s},{:02X}".format(rstr[r0s], d)

    def loadmi(self, disass=False):
        d = self.c.fetch()
        self.c.wrmem(self.c.r[rpHL], d)
        if not disass:
            return
        return "LD (HL),{:02X}".format(d)

    def loadxmi(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.fetch()
        a = adddsp(self.c.r[rpIX], dsp)
        self.c.wrmem(a, d)
        if not disass:
            return
        return "LD (IX+{:02X}),{:02X}".format(dsp, d)

    def loadymi(self, disass=False):
        dsp = self.c.fetch()
        d = self.c.fetch()
        a = adddsp(self.c.r[rpIY], dsp)
        self.c.wrmem(a, d)
        if not disass:
            return
        return "LD (IY+{:02X}),{:02X}".format(dsp, d)

    def loadrpi(self, disass=False):
        rps = rpname[self.c.rp]
        d = self.c.fetch16()
        self.c.r[rps] = d
        if not disass:
            return
        return "LD {:s},{:04X}".format(rstr[rps], d)

    def loadrpxi(self, disass=False):
        rps = rpxname[self.c.rp]
        d = self.c.fetch16()
        self.c.r[rps] = d
        if not disass:
            return
        return "LD {:s},{:04X}".format(rstr[rps], d)

    def loadrpyi(self, disass=False):
        rps = rpyname[self.c.rp]
        d = self.c.fetch16()
        self.c.r[rps] = d
        if not disass:
            return
        return "LD {:s},{:04X}".format(rstr[rps], d)

    def loadrpa(self, disass=False):
        rps = rpname[self.c.rp]
        self.c.wrmem(self.c.r[rps], self.c.r[rA])
        if not disass:
            return
        return "LD ({:s}),A".format(rstr[rps])

    def loadarp(self, disass=False):
        rps = rpname[self.c.rp]
        self.c.r[rA] = self.c.rdmem(self.c.r[rps])
        if not disass:
            return
        return "LD A,({:s})".format(rstr[rps])

    def loadna(self, disass=False):
        a = self.c.fetch16()
        self.c.wrmem(a, self.c.r[rA])
        if not disass:
            return
        return "LD ({:04X}),A".format(a)

    def loadan(self, disass=False):
        a = self.c.fetch16()
        self.c.r[rA] = self.c.rdmem(a)
        if not disass:
            return
        return "LD A,({:04X})".format(a)

    def loadnrp(self, disass=False):
        rps = rpname[self.c.rp]
        a = self.c.fetch16()
        self.c.wrmem16(a, self.c.r[rps])
        if not disass:
            return
        return "LD ({:04X}),{:s}".format(a, rstr[rps])

    def loadrpn(self, disass=False):
        rps = rpname[self.c.rp]
        a = self.c.fetch16()
        self.c.r[rps] = self.c.rdmem16(a)
        if not disass:
            return
        return "LD {:s},({:04X})".format(rstr[rps], a)

    def loadnrpx(self, disass=False):
        rps = rpxname[self.c.rp]
        a = self.c.fetch16()
        self.c.wrmem16(a, self.c.r[rps])
        if not disass:
            return
        return "LD ({:04X}),{:s}".format(a, rstr[rps])

    def loadrpxn(self, disass=False):
        rps = rpxname[self.c.rp]
        a = self.c.fetch16()
        self.c.r[rps] = self.c.rdmem16(a)
        if not disass:
            return
        return "LD {:s},({:04X})".format(rstr[rps], a)

    def loadnrpy(self, disass=False):
        rps = rpyname[self.c.rp]
        a = self.c.fetch16()
        self.c.wrmem16(a, self.c.r[rps])
        if not disass:
            return
        return "LD ({:04X}),{:s}".format(a, rstr[rps])

    def loadrpyn(self, disass=False):
        rps = rpyname[self.c.rp]
        a = self.c.fetch16()
        self.c.r[rps] = self.c.rdmem16(a)
        if not disass:
            return
        return "LD {:s},({:04X})".format(rstr[rps], a)

    def loadsphl(self, disass=False):
        self.c.r[rpSP] = self.c.r[rpHL]
        if not disass:
            return
        return "LD SP,HL"

    def loadspix(self, disass=False):
        self.c.r[rpSP] = self.c.r[rpIX]
        if not disass:
            return
        return "LD SP,IX"

    def loadspiy(self, disass=False):
        self.c.r[rpSP] = self.c.r[rpIY]
        if not disass:
            return
        return "LD SP,IY"

    def ldia(self, disass=False):
        self.c.r[rI] = self.c.r[rA]
        if not disass:
            return
        return "LD I,A"

    def ldai(self, disass=False):
        d = self.c.r[rI]
        i = self.c.iff2
        self.c.r[rA] = d
        self.c.r[rF] = (logf(d) & 0xfa) | self.c.r[fC] | (i << 2)
        if not disass:
            return
        return "LD A,I"

    def ldra(self, disass=False):
        self.c.r[rR] = self.c.r[rA]
        if not disass:
            return
        return "LD R,A"

    def ldar(self, disass=False):
        d = self.c.r[rR]
        i = self.c.iff2
        self.c.r[rA] = d
        self.c.r[rF] = (logf(d) & 0xfa) | self.c.r[fC] | (i << 2)
        if not disass:
            return
        return "LD A,R"

    def exa(self, disass=False):
        self.c.r.exa()
        if not disass:
            return
        return "EX AF,AF'"

    def exx(self, disass=False):
        self.c.r.exx()
        if not disass:
            return
        return "EXX"

    def exdehl(self, disass=False):
        d = self.c.r[rpDE]
        self.c.r[rpDE] = self.c.r[rpHL]
        self.c.r[rpHL] = d
        if not disass:
            return
        return "EX DE,HL"

    def exsphl(self, disass=False):
        a = self.c.r[rpSP]
        d = self.c.rdmem(a)
        self.c.wrmem(a, self.c.r[rpHL])
        self.c.r[rpHL] = d
        if not disass:
            return
        return "EX (SP),HL"

    def exspix(self, disass=False):
        a = self.c.r[rpSP]
        d = self.c.rdmem(a)
        self.c.wrmem(a, self.c.r[rpIX])
        self.c.r[rpIX] = d
        if not disass:
            return
        return "EX (SP),IX"

    def exspiy(self, disass=False):
        a = self.c.r[rpSP]
        d = self.c.rdmem(a)
        self.c.wrmem(a, self.c.r[rpIY])
        self.c.r[rpIY] = d
        if not disass:
            return
        return "EX (SP),IY"

    def getinstr(self):
        rv = {}

        # load r, r
        for r0 in [0, 1, 2, 3, 4, 5, 7]:
            for r1 in [0, 1, 2, 3, 4, 5, 7]:
                rv.update({bytes([0x40 | (r0 << 3) | r1]): self.loadrr})
                rv.update({bytes([0xdd, 0x40 | (r0 << 3) | r1]): self.loadxx})
                rv.update({bytes([0xfd, 0x40 | (r0 << 3) | r1]): self.loadyy})

        # load r,m; load m,r; load r,imm
        for r0 in [0, 1, 2, 3, 4, 5, 7]:
            rv.update({bytes([0x46 | (r0 << 3)]): self.loadrm})
            rv.update({bytes([0xdd, 0x46 | (r0 << 3)]): self.loadrxm})
            rv.update({bytes([0xfd, 0x46 | (r0 << 3)]): self.loadrym})
            rv.update({bytes([0x70 | r0]): self.loadmr})
            rv.update({bytes([0xdd, 0x70 | r0]): self.loadxmr})
            rv.update({bytes([0xfd, 0x70 | r0]): self.loadymr})
            rv.update({bytes([0x6 | (r0 << 3)]): self.loadri})
            rv.update({bytes([0xdd, 0x6 | (r0 << 3)]): self.loadrxi})
            rv.update({bytes([0xfd, 0x6 | (r0 << 3)]): self.loadryi})

        # load m,imm; load xm,imm; load ym,imm
        rv.update({bytes([0x36]): self.loadmi})
        rv.update({bytes([0xdd, 0x36]): self.loadxmi})
        rv.update({bytes([0xfd, 0x36]): self.loadymi})

        # load rp,imm
        for rp in range(4):
            rv.update({bytes([0x01 | (rp << 4)]): self.loadrpi})
            rv.update({bytes([0xDD, 0x01 | (rp << 4)]): self.loadrpxi})
            rv.update({bytes([0xFD, 0x01 | (rp << 4)]): self.loadrpyi})

        # load (rp),a; load a,(rp)
        for rp in range(2):
            rv.update({bytes([0x02 | (rp << 4)]): self.loadrpa})
            rv.update({bytes([0xDD, 0x02 | (rp << 4)]): self.loadrpa})
            rv.update({bytes([0xFD, 0x02 | (rp << 4)]): self.loadrpa})
            rv.update({bytes([0x0A | (rp << 4)]): self.loadarp})
            rv.update({bytes([0xDD, 0x0A | (rp << 4)]): self.loadarp})
            rv.update({bytes([0xFD, 0x0A | (rp << 4)]): self.loadarp})

        # load (ind),a; load a,(ind)
        rv.update({bytes([0x32]): self.loadna})
        rv.update({bytes([0xDD, 0x32]): self.loadna})
        rv.update({bytes([0xFD, 0x32]): self.loadna})
        rv.update({bytes([0x3A]): self.loadan})
        rv.update({bytes([0xDD, 0x3A]): self.loadan})
        rv.update({bytes([0xFD, 0x3A]): self.loadan})

        # load (ind),hl; load hl,(ind)
        rv.update({bytes([0x22]): self.loadnrp})
        rv.update({bytes([0x2A]): self.loadrpn})
        rv.update({bytes([0xDD, 0x22]): self.loadnrpx})
        rv.update({bytes([0xDD, 0x2A]): self.loadrpxn})
        rv.update({bytes([0xFD, 0x22]): self.loadnrpy})
        rv.update({bytes([0xFD, 0x2A]): self.loadrpyn})

        # load (ind),rp; load rp,(ind)
        for rp in range(4):
            rv.update({bytes([0xED, 0x43 | (rp << 4)]): self.loadnrp})
            rv.update({bytes([0xED, 0x4B | (rp << 4)]): self.loadrpn})

        rv.update({bytes([0xF9]): self.loadsphl})
        rv.update({bytes([0xDD, 0xF9]): self.loadspix})
        rv.update({bytes([0xFD, 0xF9]): self.loadspiy})

        rv.update({bytes([0xED, 0x47]): self.ldia})
        rv.update({bytes([0xED, 0x57]): self.ldai})
        rv.update({bytes([0xED, 0x4F]): self.ldra})
        rv.update({bytes([0xED, 0x5F]): self.ldar})

        rv.update({bytes([0x08]): self.exa})
        rv.update({bytes([0xDD, 0x08]): self.exa})
        rv.update({bytes([0xFD, 0x08]): self.exa})
        rv.update({bytes([0xD9]): self.exx})
        rv.update({bytes([0xDD, 0xD9]): self.exx})
        rv.update({bytes([0xFD, 0xD9]): self.exx})
        rv.update({bytes([0xEB]): self.exdehl})
        rv.update({bytes([0xDD, 0xEB]): self.exdehl})
        rv.update({bytes([0xFD, 0xEB]): self.exdehl})

        rv.update({bytes([0xE3]): self.exsphl})
        rv.update({bytes([0xDD, 0xE3]): self.exspix})
        rv.update({bytes([0xFD, 0xE3]): self.exspiy})

        return rv
