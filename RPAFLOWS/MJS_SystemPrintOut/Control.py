import MJS_SystemPrintOut
import threading

try:
    import Tkinter as tk
except:
    import tkinter as tk
    
import time

class control():
    def __init__(self,):
        self.loop = 0
        self.looptime = 0
        self.root = tk.Tk()
        self.label = tk.Label(text="", font=('Helvetica', 48), fg='red')
        self.label.pack()
        self.countvar = tk.StringVar()
        self.counter = tk.Label(textvariable=self.countvar, font=('Helvetica', 48), fg='blue')
        self.counter.pack()

        self.update_clock()
        # self.limit()
        # self.threadstart()
        self.root.mainloop()

    def threadstart(self):
        if self.looptime >= 1 and self.looptime <= 5:
            self.thread = threading.Thread(target=MJS_SystemPrintOut.call(self))
            self.thread.start()
        elif self.looptime >= 30:
            self.thread
        self.root.update()
        self.root.after(1000, self.threadstart)

    def update_clock(self):
        self.loop += 1
        if self.loop == 5:
            self.looptime += self.loop
            self.loop = 0
            self.countvar.set(str(self.looptime))        
        now = time.strftime("%H:%M:%S")
        self.label.configure(text=now)
        self.root.update()
        self.root.after(1000, self.update_clock)

    def reset(self):
        self.looptime = 0
        self.countvar.set(str(self.looptime))
        self.root.update()        

    def limit(self):
        if self.looptime >= 30:
            self.looptime = 0
            self.countvar.set(str(self.looptime))
        self.root.update()
        self.root.after(1000, self.limit)

if __name__ == "__main__":
    app=control()