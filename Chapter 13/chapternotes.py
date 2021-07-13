import tkinter
import tkinter.messagebox

#
# class MyGui:
#     def __init__(self):
#         self.main_Window = tkinter.Tk()
#         self.label = tkinter.Label(self.main_Window, text='Hello World!')
#         self.label2 = tkinter.Label(self.main_Window, text='This is the poop stain')
#         self.label.pack(side='left')
#         self.label2.pack(side='left')
#         tkinter.mainloop()
#
#
# my_gui = MyGui()


# class MyGui:
#     def __init__(self):
#         self.main_Window = tkinter.Tk()
#
#         self.frame_1 = tkinter.Frame(self.main_Window)
#
#         self.label_1_1 = tkinter.Label(self.frame_1, text='1')
#         self.label_1_2 = tkinter.Label(self.frame_1, text='2')
#         self.label_1_3 = tkinter.Label(self.frame_1, text='3')
#
#         self.label_1_1.pack(side='top')
#         self.label_1_2.pack(side='top')
#         self.label_1_3.pack(side='top')
#
#         self.frame_1.pack()
#
#         self.frame_2 = tkinter.Frame(self.main_Window)
#
#         self.label_2_1 = tkinter.Label(self.frame_2, text='1')
#         self.label_2_2 = tkinter.Label(self.frame_2, text='2')
#         self.label_2_3 = tkinter.Label(self.frame_2, text='3')
#
#         self.label_2_1.pack(side='left')
#         self.label_2_2.pack(side='left')
#         self.label_2_3.pack(side='left')
#
#         self.frame_2.pack()
#
#         tkinter.mainloop()
#
#
# my_Gui = MyGui()


# class MyGui:
#     def __init__(self):
#         self.main_Window = tkinter.Tk()
#
#         self.my_Button = tkinter.Button(self.main_Window, text='Click Me!', command=self.do_Something)
#         self.my_Button.pack()
#
#         tkinter.mainloop()
#
#     def do_Something(self):
#         tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button.')
#
#
# my_Gui = MyGui()


# class MyGui:
#     def __init__(self):
#         self.main_Window = tkinter.Tk()
#
#         self.my_button = tkinter.Button(self.main_Window, text='click me!', command=self.do_Something)
#
#         self.quit_Button = tkinter.Button(self.main_Window, text='Quit', command=self.main_Window.destroy)
#
#         self.my_button.pack()
#         self.quit_Button.pack()
#
#         tkinter.mainloop()
#
#     def do_Something(self):
#         tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button!')
#
#
# my_Gui = MyGui()


# class MyGui:
#     def __init__(self):
#         self.main_Window = tkinter.Tk()
#
#         self.frame_1 = tkinter.Frame(self.main_Window)
#         self.frame_2 = tkinter.Frame(self.main_Window)
#
#         self.label_1 = tkinter.Label(self.frame_1, text='Enter a distance in kilometers: ')
#         self.entry_1 = tkinter.Entry(self.frame_1, width=10)
#
#         self.label_1.pack(side='left')
#         self.entry_1.pack(side='left')
#
#         self.button_1 = tkinter.Button(self.frame_2, text='Convert', command=self.convert)
#         self.quit_Button = tkinter.Button(self.frame_2, text='quit', command=self.main_Window.destroy)
#
#         self.button_1.pack(side='left')
#         self.quit_Button.pack(side='left')
#
#         self.frame_1.pack()
#         self.frame_2.pack()
#
#         tkinter.mainloop()
#
#     def convert(self):
#         kilo = float(self.entry_1.get())
#         miles = kilo * 0.6214
#         tkinter.messagebox.showinfo('Answer', str(kilo) + ' kilometers is equal to ' + str(miles) + ' miles.')
#
#
# my_Gui = MyGui()


# class KiloConverterGUI:
#     def __init__(self):
#         self.main_Window = tkinter.Tk()
#
#         self.top_frame = tkinter.Frame()
#         self.mid_frame = tkinter.Frame()
#         self.bottom_frame = tkinter.Frame()
#
#         self.prompt_label = tkinter.Label(self.top_frame, text='Enter a distance in kilometers:')
#         self.kilo_entry = tkinter.Entry(self.top_frame, width=10)
#
#         self.prompt_label.pack(side='left')
#         self.kilo_entry.pack(side='left')
#
#         self.descr_label = tkinter.Label(self.mid_frame, text='Converted to miles:')
#         self.value = tkinter.StringVar()
#
#         self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.value)
#
#         self.descr_label.pack(side='left')
#         self.miles_label.pack(side='left')
#
#         self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
#         self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_Window.destroy)
#
#         self.calc_button.pack(side='left')
#         self.quit_button.pack(side='left')
#
#         self.top_frame.pack()
#         self.mid_frame.pack()
#         self.bottom_frame.pack()
#
#         tkinter.mainloop()
#
#     def convert(self):
#         kilo = float(self.kilo_entry.get())
#
#         miles = kilo * 0.6214
#
#         self.value.set(miles)
#
#
# kilo_conv = KiloConverterGUI()



