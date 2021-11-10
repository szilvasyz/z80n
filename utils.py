rpoffs = 50
flagoffs = 100

rB = 0
rC = 1
rD = 2
rE = 3
rH = 4
rL = 5
rA = 6
rF = 7
rB_ = 8
rC_ = 9
rD_ = 10
rE_ = 11
rH_ = 12
rL_ = 13
rA_ = 14
rF_ = 15
rXH = 16
rXL = 17
rYH = 18
rYL = 19
rR = 20
rI = 21
rpSP = 22
rpPC = 23
rpBC = rB + rpoffs
rpDE = rD + rpoffs
rpHL = rH + rpoffs
rpAF = rA + rpoffs
rpBC_ = rB_ + rpoffs
rpDE_ = rD_ + rpoffs
rpHL_ = rH_ + rpoffs
rpAF_ = rA_ + rpoffs
rpIX = rXH + rpoffs
rpIY = rYH + rpoffs

fS = flagoffs + 0b10000000
fZ = flagoffs + 0b01000000
f5 = flagoffs + 0b00100000
fH = flagoffs + 0b00010000
f3 = flagoffs + 0b00001000
fP = flagoffs + 0b00000100
fN = flagoffs + 0b00000010
fC = flagoffs + 0b00000001


rname = [rB, rC, rD, rE, rH, rL, -1, rA]
rxname = [rB, rC, rD, rE, rXH, rXL, -1, rA]
ryname = [rB, rC, rD, rE, rYH, rYL, -1, rA]
rpname = [rpBC, rpDE, rpHL, rpSP]
rpxname = [rpBC, rpDE, rpIX, rpSP]
rpyname = [rpBC, rpDE, rpIY, rpSP]
rp2name = [rpBC, rpDE, rpHL, rpAF]
rp2xname = [rpBC, rpDE, rpIX, rpAF]
rp2yname = [rpBC, rpDE, rpIY, rpAF]

rstr = {
    rB: "B", rC: "C", rD: "D", rE: "E",
    rH: "H", rL: "L", rA: "A", rF: "F",
    rB_: "B'", rC_: "C'", rD_: "D'", rE_: "E'",
    rH_: "H'", rL_: "L'", rA_: "A'", rF_: "F'",
    rXH: "XH", rXL: "XL", rYH: "YH", rYL: "YL",
    rR: "R", rI: "I", rpSP: "SP", rpPC: "PC",
    rpBC: "BC", rpDE: "DE", rpHL: "HL", rpAF: "AF",
    rpBC_: "BC'", rpDE_: "DE'", rpHL_: "HL'", rpAF_: "AF'",
    rpIX: "IX", rpIY: "IY"
}


def readscr(mem, addr):
    s = ""
    for i in range(192):
        for j in range(32):
            b = mem[addr + 32 * i + j]
            for k in range(8):
                s += "O" if b & 0x80 else " "
                b <<= 1
        s += "\n"
    return s


def add8(op1, op2, cy):
    res = lobyte(op1 + op2 + cy)
    f = 0
    f |= ((op1 & 0xF) + (op2 & 0xF) + cy) & 0x10  # h
    f |= (op1 + op2 + cy) >> 8  # c
    f |= res & 0x80  # s
    f |= 0 if (op1 ^ op2) & 0x80 else ((op1 ^ res) >> 5) & 0x4  # v
    f |= 0 if res else 0x40  # z
    f |= res & 0x28  # f3, f5
    return [res, f]


def sub8(op1, op2, cy):
    res = lobyte(op1 - op2 - cy)
    f = 2  # n
    f |= ((op1 & 0xF) - (op2 & 0xF) - cy) & 0x10  # h
    f |= ((op1 - op2 - cy) >> 8) & 1  # c
    f |= res & 0x80  # s
    f |= ((op1 ^ res) >> 5) & 0x4 if (op1 ^ op2) & 0x80 else 0  # v
    f |= 0 if res else 0x40  # z
    f |= res & 0x28  # f3, f5
    return [res, f]


def add16(op1, op2, cy):
    res = op1 + op2 + cy
    f = 0
    f |= (((op1 & 0xFFF) + (op2 & 0xFFF) + cy) & 0x1000) >> 8  # h
    f |= 1 if res > 0xFFFF else 0  # c
    f |= 0x80 if res & 0x8000 else 0  # s
    f |= 0 if (op1 ^ op2) & 0x8000 else ((op1 ^ res) >> 13) & 0x4  # v
    res &= 0xFFFF
    f |= 0 if res else 0x40  # z
    f |= (res & 0x2800) >> 8  # f3, f5
    return [res, f]


def sub16(op1, op2, cy):
    res = op1 - op2 - cy
    f = 2  # n
    f |= 0x10 if ((op1 & 0xFFF) - (op2 & 0xFFF) - cy) < 0 else 0  # h
    f |= 1 if res < 0 else 0  # c
    f |= 0x80 if res & 0x8000 else 0  # s
    f |= ((op1 ^ res) >> 13) & 0x4 if (op1 ^ op2) & 0x8000 else 0  # v
    res &= 0xFFFF
    f |= 0 if res else 0x40  # z
    f |= (res & 0x2800) >> 8  # f3, f5
    return [res, f]


def rotfun(d, c, fun):
    rv = fun(d, c)
    rv[0] &= 0xFF
    rv[1] = (rv[1] & 0x01) | logf(rv[0])
    return rv


def logf(op):
    p = op ^ (op >> 4)
    p = p ^ (p >> 2)
    p = p ^ (p >> 1)
    f = 0 if p & 1 else 4
    f |= op & 0x80  # s
    f |= 0 if op else 0x40  # z
    f |= op & 0x08  # f3
    f |= op & 0x20  # f5
    return f


def lobyte(i):
    return i & 0xFF


def hibyte(i):
    return (i >> 8) & 0xff


def word(i):
    return i & 0xFFFF


def mkword(h, l):
    return (lobyte(h) << 8) | lobyte(l)


def signdsp(d):
    if d & 0x80:
        d = d - 0x100
    return d


def adddsp(a, d):
    return word(a + signdsp(d))


def inc8(i):
    return lobyte(i + 1)


def dec8(i):
    return lobyte(i - 1)


def inc16(i):
    return word(i + 1)


def dec16(i):
    return word(i - 1)


