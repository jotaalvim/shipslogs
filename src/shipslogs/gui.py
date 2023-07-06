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
    save.configure(fg_color='#7aeb7a')
    helpergui.setSettings((
        nameEntry.get(),
        pathIEntry.get(),
        pathOEntry.get(),
        dateFormatEntry.get() ))


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
width  = 800

ix = 100#width - 60*3
iy = 100#height - 60*3
#print(ix,iy)

root.geometry(f'{width}x{height}')
root.title("Ship's Diary")


my_font = ('Arial',20)

#===============================================================================


def clear_frame():
    for widgets in root.winfo_children():
        #print(widgets)
        widgets.destroy()




def settings():
    clear_frame()
    global frame
    global nameEntry
    global pathIEntry
    global pathOEntry
    global dateFormatEntry
    global save

    aname, out, sin, date = helpergui.getSettings()

    frame = customtkinter.CTkFrame(master=root)
    frame.grid(row=0, column=0,pady=60,padx=60,ipadx=ix, ipady=iy)

    ships = customtkinter.CTkLabel(master=frame, text='Ship\'s Diary',font=('Roboto',26))
    ships.grid(row=0, column=2,pady=12,padx=12)

    # FIXME label
    labelS = customtkinter.CTkLabel(master=frame, text='Settings',font=my_font)
    labelS.grid(row=1, column=0,pady=12,padx=12)

    name = customtkinter.CTkLabel(master=frame, text='Authors Name',font=my_font)
    name.grid(row=2, column=0,pady=12,padx=12)

    nameEntry = customtkinter.CTkEntry(master=frame,placeholder_text=aname,font=my_font,width = 400)
    nameEntry.grid(row=2, column=1,columnspan=2,pady=12,padx=12)
    nameEntry.insert(0,aname)

    pathInput = customtkinter.CTkLabel(master=frame, text='ScreenShot Input',font=my_font)
    pathInput.grid(row=3, column=0,pady=12,padx=12)

    pathIEntry = customtkinter.CTkEntry(master=frame,placeholder_text=sin,font=my_font,width = 400)
    pathIEntry.grid(row=3, column=1,columnspan=2,pady=12,padx=12)
    pathIEntry.insert(0,sin)

    pathOutput = customtkinter.CTkLabel(master=frame, text='Diary Output',font=my_font)
    pathOutput.grid(row=4, column=0,pady=12,padx=12)

    pathOEntry = customtkinter.CTkEntry(master=frame,placeholder_text=out,font=my_font,width = 400)
    pathOEntry.grid(row=4, column=1,columnspan=2,pady=12,padx=12)
    pathOEntry.insert(0,out)

    dateFormat = customtkinter.CTkLabel(master=frame, text='Date format',font=my_font)
    dateFormat.grid(row=5, column=0,pady=12,padx=12)

    dateFormatEntry = customtkinter.CTkEntry(master=frame,placeholder_text=date,font=my_font,width = 400)
    dateFormatEntry.grid(row=5, column=1,columnspan=2,pady=12,padx=12)
    dateFormatEntry.insert(0,date)



    save = customtkinter.CTkButton(master=frame, text='Save',command=saveSettings,font=my_font)
    save.grid(row=6, column=3,pady=12,padx=12)
    save.configure(fg_color='#7aeb7a',text_color = 'black')

    back = customtkinter.CTkButton(master=frame, text='Back',command=main,font=my_font,text_color = 'black')
    back.grid(row=6, column=0,pady=12,padx=12)

#===============================================================================


def main():
    
    global entry1

    clear_frame()
    

    frame = customtkinter.CTkFrame(master=root)
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


    if helpergui.setFormat("pdf"):
        switch_1.select(1)
    if helpergui.setFormat("docx"):
        switch_2.select(1)
    if helpergui.setFormat("pptx"):
        switch_3.select(1)
    if helpergui.setFormat("html"):
        switch_4.select(1)
    if helpergui.setFormat("latex"):
        switch_5.select(1)

main()
root.mainloop()
