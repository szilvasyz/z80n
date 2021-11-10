#
# Z80 jumps and branches
#


from utils import *


class jump:

    def __init__(self, parent):
        self.c = parent


    def djnz(self, disass=False):
        dsp = self.c.fetch()
        a = adddsp(self.c.r[rpPC], dsp)
        d = lobyte(self.c.r[rB] - 1)
        self.c.r[rB] = d
        if d != 0:
            self.c.r[rpPC] = a
        if not disass:
            return
        return "DJNZ {:04X}".format(a)

    def jr(self, disass=False):
        dsp = self.c.fetch()
        a = adddsp(self.c.r[rpPC], dsp)
        self.c.r[rpPC] = a
        if not disass:
            return
        return "JR {:04X}".format(a)

    def jrnz(self, disass=False):
        dsp = self.c.fetch()
        a = adddsp(self.c.r[rpPC], dsp)
        if not self.c.r[fZ]:
            self.c.r[rpPC] = a
        if not disass:
            return
        return "JR NZ,{:04X}".format(a)

    def jrz(self, disass=False):
        dsp = self.c.fetch()
        a = adddsp(self.c.r[rpPC], dsp)
        if self.c.r[fZ]:
            self.c.r[rpPC] = a
        if not disass:
            return
        return "JR Z,{:04X}".format(a)

    def jrnc(self, disass=False):
        dsp = self.c.fetch()
        a = adddsp(self.c.r[rpPC], dsp)
        if not self.c.r[fC]:
            self.c.r[rpPC] = a
        if not disass:
            return
        return "JR NC,{:04X}".format(a)

    def jrc(self, disass=False):
        dsp = self.c.fetch()
        a = adddsp(self.c.r[rpPC], dsp)
        if self.c.r[fC]:
            self.c.r[rpPC] = a
        if not disass:
            return
        return "JR C,{:04X}".format(a)

    def jp(self, disass=False):
        a = self.c.fetch16()
        self.c.r[rpPC] = a
        if not disass:
            return
        return "JP {:04X}".format(a)

    def jphl(self, disass=False):
        a = self.c.r[rpHL]
        self.c.r[rpPC] = a
        if not disass:
            return
        return "JP HL"

    def jpix(self, disass=False):
        a = self.c.r[rpIX]
        self.c.r[rpPC] = a
        if not disass:
            return
        return "JP IX"

    def jpiy(self, disass=False):
        a = self.c.r[rpIY]
        self.c.r[rpPC] = a
        if not disass:
            return
        return "JP IY"

    def jpnz(self, disass=False):
        a = self.c.fetch16()
        if not self.c.r[fZ]:
            self.c.r[rpPC] = a
        if not disass:
            return
        return "JP NZ,{:04X}".format(a)

    def jpz(self, disass=False):
        a = self.c.fetch16()
        if self.c.r[fZ]:
            self.c.r[rpPC] = a
        if not disass:
            return
        return "JP Z,{:04X}".format(a)

    def jpnc(self, disass=False):
        a = self.c.fetch16()
        if not self.c.r[fC]:
            self.c.r[rpPC] = a
        if not disass:
            return
        return "JP NC,{:04X}".format(a)

    def jpc(self, disass=False):
        a = self.c.fetch16()
        if self.c.r[fC]:
            self.c.r[rpPC] = a
        if not disass:
            return
        return "JP C,{:04X}".format(a)

    def jppo(self, disass=False):
        a = self.c.fetch16()
        if not self.c.r[fP]:
            self.c.r[rpPC] = a
        if not disass:
            return
        return "JP PO,{:04X}".format(a)

    def jppe(self, disass=False):
        a = self.c.fetch16()
        if self.c.r[fP]:
            self.c.r[rpPC] = a
        if not disass:
            return
        return "JP PE,{:04X}".format(a)

    def jpp(self, disass=False):
        a = self.c.fetch16()
        if not self.c.r[fS]:
            self.c.r[rpPC] = a
        if not disass:
            return
        return "JP P,{:04X}".format(a)

    def jpm(self, disass=False):
        a = self.c.fetch16()
        if self.c.r[fS]:
            self.c.r[rpPC] = a
        if not disass:
            return
        return "JP M,{:04X}".format(a)

    def getinstr(self):
        rv = {}

        # djnz, jr, jrnz, jrz, jrnc, jrc
        rv.update({b'\x10': self.djnz})
        rv.update({b'\xdd\x10': self.djnz})
        rv.update({b'\xfd\x10': self.djnz})
        rv.update({b'\x18': self.jr})
        rv.update({b'\xdd\x18': self.jr})
        rv.update({b'\xfd\x18': self.jr})
        rv.update({b'\x20': self.jrnz})
        rv.update({b'\xdd\x20': self.jrnz})
        rv.update({b'\xfd\x20': self.jrnz})
        rv.update({b'\x28': self.jrz})
        rv.update({b'\xdd\x28': self.jrz})
        rv.update({b'\xfd\x28': self.jrz})
        rv.update({b'\x30': self.jrnc})
        rv.update({b'\xdd\x30': self.jrnc})
        rv.update({b'\xfd\x30': self.jrnc})
        rv.update({b'\x38': self.jrc})
        rv.update({b'\xdd\x38': self.jrc})
        rv.update({b'\xfd\x38': self.jrc})

        # jp, jphl
        rv.update({b'\xc3': self.jp})
        rv.update({b'\xdd\xc3': self.jp})
        rv.update({b'\xfd\xc3': self.jp})
        rv.update({b'\xE9': self.jphl})
        rv.update({b'\xdd\xE9': self.jpix})
        rv.update({b'\xfd\xE9': self.jpiy})

        # jp, jpnz, jpz, jpnc, jpc, jppo, jppe, jpp, jpm
        rv.update({b'\xc3': self.jp})
        rv.update({b'\xdd\xc3': self.jp})
        rv.update({b'\xfd\xc3': self.jp})
        rv.update({b'\xc2': self.jpnz})
        rv.update({b'\xdd\xc2': self.jpnz})
        rv.update({b'\xfd\xc2': self.jpnz})
        rv.update({b'\xca': self.jpz})
        rv.update({b'\xdd\xca': self.jpz})
        rv.update({b'\xfd\xca': self.jpz})
        rv.update({b'\xd2': self.jpnc})
        rv.update({b'\xdd\xd2': self.jpnc})
        rv.update({b'\xfd\xd2': self.jpnc})
        rv.update({b'\xda': self.jpc})
        rv.update({b'\xdd\xda': self.jpc})
        rv.update({b'\xfd\xda': self.jpc})
        rv.update({b'\xe2': self.jppo})
        rv.update({b'\xdd\xe2': self.jppo})
        rv.update({b'\xfd\xe2': self.jppo})
        rv.update({b'\xea': self.jppe})
        rv.update({b'\xdd\xea': self.jppe})
        rv.update({b'\xfd\xea': self.jppe})
        rv.update({b'\xf2': self.jpp})
        rv.update({b'\xdd\xf2': self.jpp})
        rv.update({b'\xfd\xf2': self.jpp})
        rv.update({b'\xfa': self.jpm})
        rv.update({b'\xdd\xfa': self.jpm})
        rv.update({b'\xfd\xfa': self.jpm})

        return rv
