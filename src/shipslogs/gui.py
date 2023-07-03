import customtkinter
import loader
import helpergui

#my_font = customtkinter.CTkFont(family="familia", size=24)
my_font = ('Arial',20)


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()

root.geometry("415x335")


def login():
    print("click teste")


frame = customtkinter.CTkFrame(master=root)
#frame.grid(row=0, column=0,pady=20,padx=60, fill='both',expand=True)
frame.grid(row=0, column=0,pady=20,padx=60)

label = customtkinter.CTkLabel(master=frame, text='Ship\'s Diary',font=('Roboto',26))

label.grid(row=0, column=0,pady=12,padx=10)


entry1 = customtkinter.CTkEntry(master=frame,placeholder_text='domain name',font=my_font)
entry1.grid(row=1, column=0,pady=12,padx=10)

entry2 = customtkinter.CTkEntry(master=frame,placeholder_text=loader.getDay(),font=my_font)
entry2.grid(row=2, column=0,pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text='Start Diary',command=login,font=my_font)
button.grid(row=3, column=0,pady=12,padx=10)


#my_font.configure(family="familia")


def switch_event1():
    helpergui.toogleFormat("pdf")

def switch_event2():
    helpergui.toogleFormat("docx")

def switch_event3():
    helpergui.toogleFormat("pptx")

def switch_event4():
    helpergui.toogleFormat("html")

def switch_event5():
    helpergui.toogleFormat("latex")




switch_1 = customtkinter.CTkSwitch(master=frame, text="pdf", command=switch_event1,font=my_font)
switch_1.grid(row=0, column=1,padx=20, pady=10)


switch_2 = customtkinter.CTkSwitch(master=frame, text="docx", command=switch_event2,font=my_font)
switch_2.grid(row=1, column=1,padx=20, pady=10)

switch_3 = customtkinter.CTkSwitch(master=frame, text="pptx", command=switch_event3,font=my_font)
switch_3.grid(row=2, column=1,padx=20, pady=10)

switch_4 = customtkinter.CTkSwitch(master=frame, text="html", command=switch_event4,font=my_font)
switch_4.grid(row=3, column=1,padx=20, pady=10)


switch_5 = customtkinter.CTkSwitch(master=frame, text="latex", command=switch_event5,font=my_font)
switch_5.grid(row=4, column=1,padx=20, pady=10)


if helpergui.set("pdf"):
    switch_1.select(1)
if helpergui.set("docx"):
    switch_2.select(1)
if helpergui.set("pptx"):
    switch_3.select(1)
if helpergui.set("html"):
    switch_4.select(1)
if helpergui.set("latex"):
    switch_5.select(1)





root.mainloop()
