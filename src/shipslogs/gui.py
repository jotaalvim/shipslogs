import customtkinter
import loader
import helpergui


#===============================================================================
count = 0
def alert():
    global count
    if count < 10:
        entry1.configure(fg_color='#FF7F7F')
        root.after(10, alert)
        count +=1
    else:
        entry1.configure(fg_color='white')
        count = 0



#===============================================================================

def saveSettings():
    print("salvar settings")


def login():
    if entry1.get() == '':
        alert()
    else:
        print("start",entry1.get())

#===============================================================================

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()

height = 585
width  = 600

ix = 100#width - 60*3
iy = 100#height - 60*3
print(ix,iy)

root.geometry(f'{width}x{height}')

my_font = ('Arial',20)

#===============================================================================


def clear_frame():
   for widgets in root.winfo_children():
      widgets.destroy()



def settings():
    clear_frame()

    frame = customtkinter.CTkFrame(master=root)
    frame.grid(row=0, column=0,pady=60,padx=60,ipadx=ix, ipady=iy)

    ships = customtkinter.CTkLabel(master=frame, text='Ship\'s Diary',font=('Roboto',26))
    ships.grid(row=0, column=2,pady=12,padx=12)

    # FIXME label de merda
    labelS = customtkinter.CTkLabel(master=frame, text='Settings',font=my_font)
    labelS.grid(row=1, column=0,pady=12,padx=12)

    name = customtkinter.CTkLabel(master=frame, text='Authors Name',font=my_font)
    name.grid(row=2, column=0,pady=12,padx=12)

    nameEntry = customtkinter.CTkEntry(master=frame,placeholder_text="John Hofstadter",font=my_font)
    nameEntry.grid(row=2, column=1,columnspan=2,pady=12,padx=12)


    pathInput = customtkinter.CTkLabel(master=frame, text='ScreenShot Input',font=my_font)
    pathInput.grid(row=3, column=0,pady=12,padx=12)

    pathIEntry = customtkinter.CTkEntry(master=frame,placeholder_text="getPathInput",font=my_font)
    pathIEntry.grid(row=3, column=1,columnspan=2,pady=12,padx=12)

    pathOutput = customtkinter.CTkLabel(master=frame, text='ScreenShot Input',font=my_font)
    pathOutput.grid(row=4, column=0,pady=12,padx=12)

    pathOEntry = customtkinter.CTkEntry(master=frame,placeholder_text="getPathoutput",font=my_font)
    pathOEntry.grid(row=4, column=1,columnspan=2,pady=12,padx=12)

    dateFormat = customtkinter.CTkLabel(master=frame, text='Date format',font=my_font)
    dateFormat.grid(row=5, column=0,pady=12,padx=12)

    dateFormatEntry = customtkinter.CTkEntry(master=frame,placeholder_text="getDateFormat",font=my_font)
    dateFormatEntry.grid(row=5, column=1,columnspan=2,pady=12,padx=12)



    save = customtkinter.CTkButton(master=frame, text='Save',command=saveSettings,font=my_font)
    save.grid(row=6, column=3,pady=12,padx=12)

    back = customtkinter.CTkButton(master=frame, text='Back',command=main,font=my_font)
    back.grid(row=6, column=0,pady=12,padx=12)

#===============================================================================


def main():
    global entry1

    clear_frame()
    

    frame = customtkinter.CTkFrame(master=root)
    #FIXME ipadx
    #frame.grid(row=0, column=0,pady=60,padx=60,ipadx=ix, ipady=iy)
    frame.grid(row=0, column=0,pady=60,padx=60,ipadx=ix, ipady=iy)

    label = customtkinter.CTkLabel(master=frame, text='Ship\'s Diary',font=('Roboto',26))
    label.grid(row=0, column=0,pady=12,padx=12)

    entry1 = customtkinter.CTkEntry(master=frame,placeholder_text='topic name',font=my_font)
    entry1.grid(row=1, column=0,pady=12,padx=12)

    entry2 = customtkinter.CTkEntry(master=frame,placeholder_text=loader.getDay(),font=my_font)
    entry2.grid(row=2, column=0,pady=12,padx=12)

    startB = customtkinter.CTkButton(master=frame, text='Start Diary',command=login,font=my_font)
    startB.grid(row=3, column=0,pady=12,padx=12)

    settingsB = customtkinter.CTkButton(master=frame, text='Settings',command=settings,font=my_font)
    settingsB.grid(row=4, column=0,pady=12,padx=12)


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

main()
root.mainloop()
