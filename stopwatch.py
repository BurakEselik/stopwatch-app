import tkinter as tk
from datetime import datetime, time, timezone

counter = 00000 #?
running = False

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
        self.start = tk.Button(self.f, text='Start', width=6, command=lambda: self.Start(self.label))
        self.stop = tk.Button(self.f, text='Stop', width=6, state='disabled', command=lambda: self.Stop())
        self.reset = tk.Button(self.f, text='Reset', width=6, state='disabled', command=lambda: self.Reset(self.label))
        self.f.pack(anchor= 'center', pady=5)
        self.start.pack(side='left')
        self.stop.pack(side='left')
        self.reset.pack(side='left')

    def counter_label(self, label):
        def count():
            if running:
                global counter

                # To manate the initial delay.
                if counter==00000:
                    display = 'Starting...'
                else:
                    tt = datetime.fromtimestamp(counter, tz=timezone.utc)
                    string = tt.strftime('%H:%M:%S')
                    display=string
                label['text'] = display

                label.after(1000, count)
                counter += 1

        # Triggering the start of the counter.
        count()
    
    #Start function of the stopwatch
    def Start(self, label):
        global running
        running = True
        self.counter_label(label)
        self.start['state'] = 'disabled'
        self.stop['state'] = 'normal'
        self.reset['state'] = 'normal'
        
    #Stop function of the stopwatch
    def Stop(self):
        global running
        self.start['state'] = 'normal'
        self.stop['state'] = 'disabled'
        self.reset['state'] = 'normal'
        running = False

    #Reset function of the stopwatch
    def Reset(self, label):
        global counter
        counter = 00000

        # if reset is pressed after pressing stop.
        if running==False:
            self.reset['state'] = 'disabled'
            label['text'] = 'Welcome!'
        
        #if reset is predded while the stopwatch is running.
        else:
            label['text'] = 'Starting...'

            


if __name__ == '__main__':
    stopwatch = StopWatch(className='Stopwatch - App')
    stopwatch.mainloop() 
