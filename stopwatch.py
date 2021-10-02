import tkinter as tk
from tkinter.constants import S

class StopWatch(tk.Tk):

    def __init__(self, className) -> None:
        super().__init__(className=className)

        #geometry
        self.title('StopWatch App')
        self.resizable(width=True, height=True)
        self.minsize(width=250, height=80)
        self.maxsize(width=400, height=180)

        #icon
        self.icon = tk.PhotoImage(file='stopwatch.png')
        self.iconphoto(False, self.icon)

        self.label = tk.Label(self, text='Welcome!', fg='black', font='Verdana 24 bold')
        self.label.pack()
        self.f = tk.Frame(self)
        start = tk.Button(self.f, text='Start', width=6, command=...)
        stop = tk.Button(self.f, width=6, state='disabled', command=...)
        reset = tk.Button(self.f, width=6, state='disabled', command=...)
        self.f.pack(anchor= 'center', pady=5)
        start.pack(side='left')
        stop.pack(side='left')
        reset.pack(side='left')



if __name__ == '__main__':
    stopwatch = StopWatch(className='Stopwatch - App')
    stopwatch.mainloop() 
