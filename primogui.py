import tkinter as tk
import time
import threading

from z80cpu_split import cpu
from mem import genmem


updateflag = False


class scr(genmem):
    def __init__(self, start):
        self.root = tk.Tk()
#        self.label = tk.Label(text="")
#        self.label.pack()
        self.photo = tk.PhotoImage(width=768, height=768)
        self.canvas = tk.Canvas(self.root, width=770, height=770)
        self.canvas.create_image(1, 1, image=self.photo, anchor=tk.NW)
        self.canvas.pack()
#        self.update_clock()
        self.start = start
        super().__init__(0, 0x1C00, False)

    def __setitem__(self, addr, data):
        a = addr - self.start
        if a in range(0x2000):
            x = a >> 5
            y = (a & 0x1F) << 3
            for b in range(8):
                c = '#FFFFFF' if data & (0x80 >> b) else '#000000'
                self.plot(c, y + b, x, 3)
            self.m[a] = data
        return

    def __getitem__(self, addr):
        return self.m[self.start + addr]

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

    def update(self):
        self.root.update()
        self.root.update_idletasks()

    def plot(self, color, x, y, m):
        self.photo.put(color, (x * m, y * m, x * m + m, y * m + m))


class proinp(genmem):

    def __getitem__(self, addr):
        a = addr & 0xFF
        self.m[a] ^= 0x20
        return self.m[a]



def updateloop():
    global updateflag
    updateflag = True
    threading.Timer(0.1, updateloop).start()


vid = scr(0xE000)
updateloop()

c = cpu()

#
# Primo
#
rom = genmem(0x0000, 0x4000, True)
ram = genmem(0x4000, 0xA000, False)
inp = proinp(0x0000, 0x0100, False)

for i in range(256):
    inp[i] = 0xFE
inp[0x20] = 0xFF

c.addmem(rom)
c.addmem(ram)
c.addmem(vid)
c.addinp(inp)
rom.load(0x0000, bytes(open("roms/PROPRIMO.rom", "rb").read()))
# rom.load(0x0000, bytes(open("roms/PR_A64-1.ROM", "rb").read()))
# rom.load(0x1000, bytes(open("roms/PR_A64-2.ROM", "rb").read()))
# rom.load(0x2000, bytes(open("roms/PR_A64-3.ROM", "rb").read()))
# rom.load(0x3000, bytes(open("roms/PR_A64-4.ROM", "rb").read()))

brkpts = []

while not c.halted:

    if updateflag:
        vid.update()
        updateflag = False

    # if c.r[rpPC] in brkpts:
    #     print("BRK at {:04X}".format(c.r[rpPC]))
    #     print(c.r)
    #     print(" --- ")

    s = c.step()
    if s:
        print(s)
        print(c)

print(c.r)

