import tkinter

class MPG:
    def __init__(self):
        #create the main window
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        #top Frame
        self.prompt_gallons = tkinter.Label(self.top_frame, text="How many gallons does your car hold: ")
        self.gallons_entry = tkinter.Entry(self.top_frame, width=15)
        self.prompt_gallons.pack(side="left")
        self.gallons_entry.pack(side="left")
        
        #middle Frame
        self.miles_prompt = tkinter.Label(self.middle_frame, text="How many miles did you travel: ")
        self.miles_entry = tkinter.Entry(self.middle_frame, width=15)
        self.miles_prompt.pack(side="left")
        self.miles_entry.pack(side="left")
        
        #bottom frame
        self.value = tkinter.StringVar()
        self.results_label = tkinter.Label(self.bottom_frame, textvariable=self.value)
        self.calc_button = tkinter.Button(self.bottom_frame, text="Calculate", command=self.calc_mpg)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)
        
        self.results_label.pack(side="top")
        self.calc_button.pack(side="left")
        self.quit_button.pack(side="left")
        
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        
        #Start the main loop
        tkinter.mainloop()
    
    def calc_mpg(self):
        gas = float(self.gallons_entry.get())
        miles = float(self.miles_entry.get())
        
        mpg = f"you get " + format(miles/gas, ".2f") + "miles per gallon"
        self.value.set(mpg)
    
    
car = MPG()