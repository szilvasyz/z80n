from z80cpu_split import cpu
from mem import genmem
from memcon import memcon
from utils import *


class vidmem(genmem):
    def __init__(self, start, scr):
        self.scr = scr
        self.start = start
        super().__init__(0, 0x1800, False)

    def __setitem__(self, addr, data):
        a = addr - self.start
        if a in range(0x1800):
            x = a >> 5
            y = (a & 0x1F) << 3
            for b in range(8):
                c = '#FFFFFF' if data & (0x80 >> b) else '#000000'
                self.scr.plot(c, y + b, x)
            self.m[a] = data
        return

    def __getitem__(self, addr):
        return self.m[self.start + addr]


def primo(scr):
    c = cpu()

    #
    # Primo
    #
    rom = genmem(0x0000, 0x4000, True)
    ram = genmem(0x4000, 0xA800, False)
    vid = vidmem(0xE800, scr)
    c.addmem(rom)
    c.addmem(ram)
    c.addmem(vid)
    rom.load(0x0000, bytes(open("roms/PR_A64-1.ROM", "rb").read()))
    rom.load(0x1000, bytes(open("roms/PR_A64-2.ROM", "rb").read()))
    rom.load(0x2000, bytes(open("roms/PR_A64-3.ROM", "rb").read()))
    rom.load(0x3000, bytes(open("roms/PR_A64-4.ROM", "rb").read()))

    brkpts = []

    while not c.halted:
        # if c.r[rpPC] in brkpts:
        #     print("BRK at {:04X}".format(c.r[rpPC]))
        #     print(c.r)
        #     print(" --- ")

        s = c.step()
        if s:
            print(s)
            print(c)

    print(c.r)
