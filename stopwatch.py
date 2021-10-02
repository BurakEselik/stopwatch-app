import tkinter as tk

class StopWatch(tk.Tk):

    def __init__(self, className) -> None:
        super().__init__(className=className)

        #geometry
        self.title('StopWatch App')
        self.resizable(width=False, height=False)
        self.geometry('200x100')



if __name__ == '__main__':
    stopwatch = StopWatch(className='Stopwatch - App')
    stopwatch.mainloop() 
