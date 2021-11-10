from utils import *
# from z80flags import flags


class registers():

    def __init__(self, cpu):
        self.cpu = cpu
        self.regs = {rB: 0, rC: 0,
                     rD: 0, rE: 0,
                     rH: 0, rL: 0,
                     rA: 0, rF: 0,
                     rI: 0, rR: 0,
                     rB_: 0, rC_: 0,
                     rD_: 0, rE_: 0,
                     rH_: 0, rL_: 0,
                     rA_: 0, rF_: 0,
                     rXH: 0, rXL: 0,
                     rYH: 0, rYL: 0,
                     rpSP: 0, rpPC: 0}

    def __setitem__(self, reg, value):

        if reg > flagoffs:
            self.setflag(reg, value)
            return

        if reg in [rpPC, rpSP]:
            self.regs[reg] = word(value)
            return

        if reg in [rpBC, rpDE, rpHL, rpAF, rpIX, rpIY]:
            self.regs[reg - rpoffs] = hibyte(value)
            self.regs[reg - rpoffs + 1] = lobyte(value)
            return

        self.regs[reg] = lobyte(value)

    def __getitem__(self, reg):

        if reg > flagoffs:
            return self.getflag(reg - flagoffs)

        if reg in [rpBC, rpDE, rpHL, rpAF, rpIX, rpIY,
                   rpBC_, rpDE_, rpHL_, rpAF_]:
            return mkword(self.regs[reg - rpoffs],
                          self.regs[reg - rpoffs + 1])

        return self.regs[reg]

    def __str__(self):
        s = "_BC_ _DE_ _HL_ _AF_ _IX_ _IY_ _PC_ _SP_ _I _R\n" \
            "{:04X} {:04X} {:04X} {:04X} {:04X} {:04X} {:04X} {:04X} {:02X} {:02X} "
        return (s.format(
            self[rpBC], self[rpDE], self[rpHL],
            self[rpAF], self[rpIX], self[rpIY],
            self[rpPC], self[rpSP], self[rI], self[rR])
        )

    def exa(self):
        t = self[rpAF]; self[rpAF] = self[rpAF_]; self[rpAF_] = t
        return

    def exx(self):
        t = self[rpBC]; self[rpBC] = self[rpBC_]; self[rpBC_] = t
        t = self[rpDE]; self[rpDE] = self[rpDE_]; self[rpDE_] = t
        t = self[rpHL]; self[rpHL] = self[rpHL_]; self[rpHL_] = t
        return

    def setflag(self, flag, bit):
        if bit:
            self[rF] |= flag
        else:
            self[rF] &= ~flag

    def getflag(self, flag):
        return 1 if self[rF] & flag else 0
