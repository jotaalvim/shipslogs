import tkinter
import customtkinter

import loader
import helpergui
import subprocess
import signal
#from tkinter import *
from PIL import  Image, ImageTk

from tkinter import filedialog
from tkinter import *


#DARK_MODE = "dark"
customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme("dark-blue")

my_font = ('Arial',20)

# FIXME IMAGE
#setting_image = ImageTk.PhotoImage(Image.open('assets/setting.png').resize((25,25),Image.ANTIALIAS))

#===============================================================================

stop = True
def start():
    global p, stop, last_subtopic_used, last_topic_used
    global stop
    if entry1.get() == '' and stop != False:
        alert()
    else:
        if stop == True:
            # FIXME path para os ficheiros?
            topic = entry1.get()
            subtopic = entry2.get()
            print("start",topic, subtopic)
            
            last_subtopic_used = subtopic
            last_topic_used = topic
            print("new start",last_topic_used , last_subtopic_used )
            #helpergui.setTopics((topic,subtopic))

            #start a subprocess
            print('python', 'main.py', topic, subtopic)
            p = subprocess.Popen(['python', 'main.py', topic, subtopic])
            startB.configure(hover_color ='#fa4646', fg_color='#FF7F7F',text='STOP Diary')
            stop = not stop
        elif not stop:
        #send the SIGTERM signal to the subprocess
            p.send_signal(signal.SIGINT)
            stop = not stop
            # FIXME
            startB.configure(hover_color ='#0666c2', fg_color='#3A7EBF',text_color = 'white',text='Start Diary')

#===============================================================================

count = 0
def alert():
    global count
    if count < 10:
        entry1.configure(fg_color='#FF7F7F')
        a.after(10, alert)
        count +=1
    else:
        entry1.configure(fg_color='white')
        count = 0


#===============================================================================

def saveSettings():
    #save.configure(fg_color='#7aeb7a')
    helpergui.setSettings((
        nameEntry.get(),
        pathIEntry.get(),
        pathOEntry.get(),
        dateFormatEntry.get() ))
    if helpergui.setFormat("pdf")   != switch_1.get():
        helpergui.toogleFormat("pdf")
    if helpergui.setFormat("docx")  != switch_2.get():
        helpergui.toogleFormat("docx")
    if helpergui.setFormat("pptx")  != switch_3.get():
        helpergui.toogleFormat("pptx")
    if helpergui.setFormat("html")  != switch_4.get():
        helpergui.toogleFormat("html")
    if helpergui.setFormat("latex") != switch_5.get():
        helpergui.toogleFormat("latex")

    


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    filename = filedialog.askdirectory()
    folder_path = filename
    pathIEntry.insert(0,folder_path)
    print(filename)

def browse_button2():
    # Allow user to select a directory and store it in global var
    # called folder_path
    filename = filedialog.askdirectory()
    folder_path = filename
    pathOEntry.insert(0,folder_path)
    print(filename)

#===============================================================================

def updateSwitch():
    if helpergui.setFormat("pdf"):  
        switch_1.select()
    else:
        switch_1.deselect()
    if helpergui.setFormat("docx"):
        switch_2.select()
    else:
        switch_2.deselect()
    if helpergui.setFormat("pptx"):
        switch_3.select()
    else:
        switch_3.deselect()
    if helpergui.setFormat("html"):
        switch_4.select()
    else:
        switch_4.deselect()
    if helpergui.setFormat("latex"):
        switch_5.select()
    else:
        switch_5.deselect()

#===============================================================================
# Global variables to keep track of the created diary when out of the home menu
last_topic_used = ''
last_subtopic_used = ''


class App(customtkinter.CTk):

    frames = {"frame1": None, "frame2": None}

    def frame1_selector(self):
        # FIXME adicionei para corrigir a cenas dos dwitches
        updateSwitch()
        App.frames["frame2"].pack_forget()
        App.frames["frame1"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
    
    def frame2_selector(self):
        App.frames["frame1"].pack_forget()
        App.frames["frame2"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
    
    def __init__(self):
        global entry1, entry2, startB, nameEntry, pathIEntry, pathOEntry, dateFormatEntry, save
        global switch_1, switch_2, switch_3, switch_4, switch_5

        super().__init__()
        
        self.title("Ship's Diary")

        #FIXME
        #self.geometry(f'{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0')
        self.geometry('920x600+0+0')


        # right side panel -> to show the frame1 or frame 2
        self.right_side_panel = customtkinter.CTkFrame(self)
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)
    
        self.right_side_container = customtkinter.CTkFrame(self.right_side_panel)#,fg_color="#000811")
        self.right_side_container.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
    

        #===============================================================================
        # SHIPS DIARY

        App.frames['frame1'] = customtkinter.CTkFrame(self)#,fg_color="red")
        #bt_from_frame1 = customtkinter.CTkButton(App.frames['frame1'], text="Test 1", command=lambda:print("test 1") )
        #bt_from_frame1.place(relx=0.5, rely=0.5, anchor='n')


        label = customtkinter.CTkLabel(App.frames['frame1'], text='🛳 Ship\'s Diary',font=('Roboto',60))
        #label.grid(row=0, column=0,pady=12,padx=12)
        label.place(relx=0.5, rely=0.26, anchor='center',)

        

        entry1 = customtkinter.CTkEntry(App.frames['frame1'],placeholder_text='topic name',font=my_font)
        #entry1.grid(row=1, column=0,pady=12,padx=12)
        entry1.place(relx=0.5, rely=0.4, anchor='center')


        entry2 = customtkinter.CTkEntry(App.frames['frame1'],placeholder_text=loader.getDay(),font=my_font)
        #entry2.grid(row=2, column=0,pady=12,padx=12)
        entry2.place(relx=0.5, rely=0.5, anchor='center')

    

        startB = customtkinter.CTkButton(App.frames['frame1'], text='Start Diary',command=start,font=my_font)
        #startB.grid(row=3, column=0,pady=12,padx=12)
        startB.place(relx=0.5, rely=0.6, anchor='center')


        if stop == False:
            startB.configure(fg_color='#FF7F7F',text='STOP Diary')
            top,sub = last_topic_used , last_subtopic_used #helpergui.getTopics()
            entry1.insert(0,top)
            if sub == '':
                entry2.configure(placeholder_text=loader.getDay())
            else: 
                entry2.insert(0,sub)


        #settingsB = customtkinter.CTkButton(App.frames['frame1'], text='Settings',command=lambda:self.frame2_selector(),font=my_font,image= setting_image,compound ="left"  )
        # FIXME
        settingsB = customtkinter.CTkButton(App.frames['frame1'], text='Settings',command=lambda:self.frame2_selector(),font=my_font,fg_color='#5e6e7d')
        #settingsB.grid(row=4, column=0,pady=12,padx=12)
        settingsB.place(relx=0.5, rely=0.9, anchor='center')
        

        #===============================================================================
        # SETTINGS

        App.frames['frame2'] = customtkinter.CTkFrame(self)

        aname, out, sin, date = helpergui.getSettings()

        ships = customtkinter.CTkLabel(App.frames['frame2'], text='Ship\'s Diary Settings',font=('Roboto',40))
        #ships.grid(row=0, column=2,pady=12,padx=12)
        ships.grid(row=0, column=2,pady=12,padx=12)
        #ships.place(relx=0.5, rely=0.1, anchor='center')



        name = customtkinter.CTkLabel(App.frames['frame2'], text='Authors Name',font=my_font)
        name.grid(row=2, column=0,pady=12,padx=12)

        nameEntry = customtkinter.CTkEntry(App.frames['frame2'],placeholder_text=aname,font=my_font,width = 500)
        nameEntry.grid(row=2, column=1,columnspan=2,pady=12,padx=12)
        nameEntry.insert(0,aname)



        # BROWSE INPUT filesystem
        buttonBrowse = customtkinter.CTkButton(App.frames['frame2'], text='browse',command=browse_button,font=my_font,width = 50)
        buttonBrowse.grid(row=3, column=3,pady=12,padx=12)

        pathInput = customtkinter.CTkLabel(App.frames['frame2'], text='ScreenShot Input',font=my_font)
        pathInput.grid(row=3, column=0,pady=12,padx=12)

        pathIEntry = customtkinter.CTkEntry(App.frames['frame2'],placeholder_text=sin,font=my_font,width = 500)
        pathIEntry.grid(row=3, column=1,columnspan=2,pady=12,padx=12)
        pathIEntry.insert(0,sin)



        # BROWSE OUTPUT filesystem
        buttonBrowse2 = customtkinter.CTkButton(App.frames['frame2'], text='browse',command=browse_button2,font=my_font,width = 50)
        buttonBrowse2.grid(row=4, column=3,pady=12,padx=12)

        pathOutput = customtkinter.CTkLabel(App.frames['frame2'], text='Diary Output',font=my_font)
        pathOutput.grid(row=4, column=0,pady=12,padx=12)

        pathOEntry = customtkinter.CTkEntry(App.frames['frame2'],placeholder_text=out,font=my_font,width = 500)
        pathOEntry.grid(row=4, column=1,columnspan=2,pady=12,padx=12)
        pathOEntry.insert(0,out)



        dateFormat = customtkinter.CTkLabel(App.frames['frame2'], text='Date format',font=my_font)
        dateFormat.grid(row=5, column=0,pady=12,padx=12)

        dateFormatEntry = customtkinter.CTkEntry(App.frames['frame2'],placeholder_text=date,font=my_font,width = 500)
        dateFormatEntry.grid(row=5, column=1,columnspan=2,pady=12,padx=12)
        dateFormatEntry.insert(0,date)


        exportFormat = customtkinter.CTkLabel(App.frames['frame2'], text='Export formats',font=('Roboto',26))
        exportFormat.grid(row=6, column=0,pady=12,padx=12)



        # FIXME
        def switch_event1():
            print("toogle pdf")
            #helpergui.toogleFormat("pdf")
        def switch_event2():
            print("toogle docx")
            #helpergui.toogleFormat("docx")
        def switch_event3():
            print("toogle pptx")
            #helpergui.toogleFormat("pptx")
        def switch_event4():
            print("toogle html")
            #helpergui.toogleFormat("html")
        def switch_event5():
            print("toogle latex")
            #helpergui.toogleFormat("latex")


        switch_1 = customtkinter.CTkSwitch(App.frames['frame2'], text="pdf", command=switch_event1,font=my_font)
        switch_1.grid(row=7, column=1,padx=20, pady=10)

        switch_2 = customtkinter.CTkSwitch(App.frames['frame2'], text="docx", command=switch_event2,font=my_font)
        switch_2.grid(row=7, column=0,padx=20, pady=10)

        switch_3 = customtkinter.CTkSwitch(App.frames['frame2'], text="pptx", command=switch_event3,font=my_font)
        switch_3.grid(row=8, column=1,padx=20, pady=10)

        switch_4 = customtkinter.CTkSwitch(App.frames['frame2'], text="html", command=switch_event4,font=my_font)
        switch_4.grid(row=8, column=0,padx=20, pady=10)

        switch_5 = customtkinter.CTkSwitch(App.frames['frame2'], text="latex", command=switch_event5,font=my_font)
        switch_5.grid(row=9, column=0,padx=20, pady=10)


        updateSwitch()

        save = customtkinter.CTkButton(App.frames['frame2'], text='Save',command=saveSettings,font=my_font)
        save.grid(row=10, column=3,pady=62,padx=12)
        #save.configure(fg_color='#7aeb7a',text_color = 'black')

        back = customtkinter.CTkButton(App.frames['frame2'], text='Back',command=lambda:self.frame1_selector(),font=my_font)
        back.grid(row=10, column=0,pady=12,padx=12)


        self.frame1_selector()

a = App()

a.mainloop()