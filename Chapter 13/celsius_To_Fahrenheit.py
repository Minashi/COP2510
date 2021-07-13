import tkinter


class MyGui:
    def __init__(self):
        self.main_Window = tkinter.Tk()

        self.top_Frame = tkinter.Frame(self.main_Window)
        self.mid_Frame = tkinter.Frame(self.main_Window)
        self.bottom_Frame = tkinter.Frame(self.main_Window)

        self.label_1 = tkinter.Label(self.top_Frame, text='Enter the Celsius temperature:')
        self.entry_1 = tkinter.Entry(self.top_Frame, width=10)

        self.label_1.pack(side='left')
        self.entry_1.pack(side='left')

        self.temp_Value = tkinter.StringVar()
        self.label_2 = tkinter.Label(self.mid_Frame, text='Fahrenheit temperature: ')
        self.label_3 = tkinter.Label(self.mid_Frame, textvariable=self.temp_Value)

        self.label_2.pack(side='left')
        self.label_3.pack(side='left')

        self.button_1 = tkinter.Button(self.bottom_Frame, text='Convert to Fahrenheit', command=self.button_Action)
        self.quit_Button = tkinter.Button(self.bottom_Frame, text='Quit', command=self.main_Window.destroy)

        self.button_1.pack(side='left')
        self.quit_Button.pack(side='left')

        self.top_Frame.pack()
        self.mid_Frame.pack()
        self.bottom_Frame.pack()

        tkinter.mainloop()

    def button_Action(self):
        celsius_Temp = float(self.entry_1.get())

        fahrenheit_Temp = celsius_Temp*9/5+32

        self.temp_Value.set(fahrenheit_Temp)


my_Gui = MyGui()
