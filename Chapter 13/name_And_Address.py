import tkinter


class MyGui:
    def __init__(self):
        self.main_Window = tkinter.Tk()

        self.top_Frame = tkinter.Frame(self.main_Window)
        self.bottom_Frame = tkinter.Frame(self.main_Window)

        self.name_Value = tkinter.StringVar()
        self.address_Value = tkinter.StringVar()

        self.label_Name = tkinter.Label(self.top_Frame, textvariable=self.name_Value)
        self.label_Address = tkinter.Label(self.top_Frame, textvariable=self.address_Value)

        self.label_Name.pack(side='top')
        self.label_Address.pack(side='top')

        self.button_1 = tkinter.Button(self.bottom_Frame, text='Show Info', command=self.button_Action)
        self.quit_Button = tkinter.Button(self.bottom_Frame, text='Quit', command=self.main_Window.destroy)

        self.button_1.pack(side='left')
        self.quit_Button.pack(side='left')

        self.top_Frame.pack()
        self.bottom_Frame.pack()

        tkinter.mainloop()

    def button_Action(self):
        self.name_Value.set('Bob')
        self.address_Value.set('123 Sesame Street Blvd')


my_Gui = MyGui()
