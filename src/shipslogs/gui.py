import customtkinter
import loader
import helpergui

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")


root = customtkinter.CTk()

root.geometry("500x600")


def login():
    print("teste")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60, fill='both',expand=True)

label = customtkinter.CTkLabel(master=frame, text='Ship\'s Diary',font=('Roboto',24))

label.pack(pady=12,padx=10)


entry1 = customtkinter.CTkEntry(master=frame,placeholder_text='domain name')
entry1.pack(pady=12,padx=10)

entry2 = customtkinter.CTkEntry(master=frame,placeholder_text=loader.getDay())
entry2.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame, text='Start Diary',command='login')
button.pack(pady=12,padx=10)



switch_var1 = customtkinter.StringVar(value=True)
switch_var2 = customtkinter.StringVar(value=True)
switch_var3 = customtkinter.StringVar(value=True)
switch_var4 = customtkinter.StringVar(value=True)

# FIXME FAZER Eventos
def switch_event1():
    helpergui.toogleFormat("pdf")

def switch_event2():
    helpergui.toogleFormat("docx")

def switch_event3():
    helpergui.toogleFormat("html")

def switch_event4():
    helpergui.toogleFormat("latex")

# FIXME find a star value for the switch

switch_1 = customtkinter.CTkSwitch(master=frame, text="pdf", command=switch_event1,
                                    onvalue=True, offvalue=False)

switch_1.pack(padx=20, pady=10)
switch_1.select(1)

switch_2 = customtkinter.CTkSwitch(master=frame, text="docx", command=switch_event2,
                                    onvalue=True, offvalue=False)
switch_2.pack(padx=20, pady=10)
switch_2.select(1)

switch_3 = customtkinter.CTkSwitch(master=frame, text="html", command=switch_event3,
                                   onvalue=True, offvalue=False)
switch_3.pack(padx=20, pady=10)
switch_3.select(1)

switch_4 = customtkinter.CTkSwitch(master=frame, text="latex", command=switch_event4,
                                    onvalue=True, offvalue=False)
switch_4.pack(padx=20, pady=10)
switch_4.select(1)


root.mainloop()
