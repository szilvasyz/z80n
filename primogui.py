from tkinter import *
import threading
import time

from z80cpu_split import cpu
from mem import genmem
from memcon import memcon
from utils import *
from primomain import primo


class gui(threading.Thread):

    def __init__(self, scr, img, main):
        threading.Thread.__init__(self)
        self.scr = scr
        self.img = img
        self.main = main

    def run(self):
        print("hello")
        self.main(self)

        while True:

            #    root.update()
            time.sleep(1)

            for i in range(128):
                self.plot('#000000', i, 100)
                self.plot('#FF0000', 128 + i, 101)
                self.plot('#00FF00', i, 0)
                self.plot('#0000FF', 128 + i, 1)

    def plot(self, color, x, y):
        self.img.put(color, (x, y))
        self.scr.pack()


root = Tk()
image = PhotoImage(width=256, height=192)
screen = Canvas(root, width=480, height=312)
screen.create_image(112, 60, image=image, anchor=NW)
screen.pack()
label = Label(root, text="Primo")
label.pack()

app = gui(screen, image, primo)
app.start()

root.mainloop()
# self.canvas.update()



