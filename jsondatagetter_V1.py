from tkinter import *
import json
import os



class window:
    
    #Global Variables
    e = [] #course Outcomes Frames
    f = [] #course Objectives Frames
    con = [] #course Outcomes Code Frames
    cone = [] #course Outcomes Code Values
    courseo = [] #course Outcomes Values
    courseobj = [] #course Objective Values
    mycolor2 = '#1788B2' #color Code
    value = 12 #grid Purposes
    listObj = {} #the Final Object 
    CO = {} #the Pre Final Object
    
    #fucntion to clear the previous frame
    def disableFrame(self):
        self.button2['state'] = NORMAL
        self.frame.pack_forget()
        newFrame()
    
    #function to create subCode
    def createSubCode(self):
        self.l1 = Label(self.frame, text = "SUBJECT CODE", font=('Helvatical bold',12)).grid(row = 2, column = 0)
        self.e1 = Frame(self.frame, highlightbackground = self.mycolor2, highlightthickness = 1, bd=0)
        self.e1.grid(row = 2, column = 1)
        self.entry1 = Entry(self.e1, width= 40, font=('Helvatical bold',12))
        self.entry1.pack()
        Label(self.frame, text = " ").grid(row = 3, column = 0)
    
    #function to create subName
    def createSubName(self):
        self.l2 = Label(self.frame, text = "SUBJECT NAME", font=('Helvatical bold',12)).grid(row = 4, column = 0)
        self.e2 = Frame(self.frame, highlightbackground = self.mycolor2, highlightthickness = 1, bd=0)
        self.e2.grid(row = 4, column = 1)
        self.entry2 = Entry(self.e2, width= 40, font=('Helvatical bold',12))
        self.entry2.pack()
        Label(self.frame, text = " ").grid(row = 5, column = 0)
    
    #function to create CourseOutcomes
    def createCourseOutcomes(self):
        self.con = []
        self.cone = []
        self.e = []
        self.courseo = []
        self.l3 = Label(self.frame, text = "ENTER COURSE OUTCOMES", font=('Helvatical bold',12)).grid(row = 6, column = 0)
        for i in range(5):
            self.con.append(Frame(self.frame, highlightbackground = self.mycolor2, highlightthickness = 1, bd=0))
            self.con[i].grid(row = 6+i, column = 1, sticky = 'w')
            self.cone.append(Entry(self.con[i], width= 7, font=('Helvatical bold',12)))
            self.cone[i].pack()
            self.e.append(Frame(self.frame, highlightbackground = self.mycolor2, highlightthickness = 1, bd=0))
            self.e[i].grid(row = 6+i, column = 1, sticky = 'e')
            self.courseo.append(Entry(self.e[i], width= 40, font=('Helvatical bold',9)))
            self.courseo[i].pack()
        Label(self.frame, text = " ").grid(row = 11, column = 0)
    
    #function to create JSON file
    def getValues(self):
        j = 0
        self.CO = {}
        self.button2['state'] = DISABLED
        self.button_border3 = Frame(self.frame, highlightbackground = self.mycolor2, highlightthickness = 1, bd=0)
        self.button_border3.grid(row = 25, column = 1,sticky='w')
        self.button3 = Button(self.button_border3, text = "QUIT", font=('Helvatical bold',12), command=root.destroy, borderwidth = 0, fg = 'black', bg = 'white', padx = '20px')
        self.button3.pack()
        self.CO.update({"subCode":self.entry2.get()})
        self.CO.update({"subName":self.entry3.get()})
        for i in range(len(self.courseo)):
            self.CO.update({self.cone[i].get():self.courseo[i].get()})
        for i in self.courseobj:
            self.CO.update({"CObj NO. {} ".format(j+1):i.get()})
            j = j + 1
        try:
            with open(os.getcwd() + "\\resrc\\details.json") as fp:
                self.listObj = json.load(fp)
        except:
            self.listObj = {}
        self.listObj.update({self.entry1.get():self.CO})
        self.jobj = json.dumps(self.listObj, indent = 4)
        with open (os.getcwd() + "\\resrc\\details.json","w") as f:
            f.write(self.jobj)    
    
    #function for courseObjective's columns
    def putColumns(self, num):
        num = int(num)
        self.f = []
        self.courseobj = []
        for i in range(num):
            self.f.append(Frame(self.frame, highlightbackground = self.mycolor2, highlightthickness = 1, bd=0))
            self.f[i].grid(row = self.value + 3 + i, column = 1)
            self.courseobj.append(Entry(self.f[i], width= 40, font=('Helvatical bold',12)))
            self.courseobj[i].pack()
        self.button1['state'] = DISABLED
        Label(self.frame, text = " ").grid(row = 24, column = 0)
        self.button_border2 = Frame(self.frame, highlightbackground = self.mycolor2, highlightthickness = 1, bd=0)
        self.button_border2.grid(row = 25, column = 1)
        self.button2 = Button(self.button_border2, text = "SUBMIT", font=('Helvatical bold',12) , command = self.getValues,borderwidth = 0, fg = 'black', bg = 'white', padx = '20px')
        self.button2.pack()
        
    #function for creating courseObjective
    def createCourseObjectives(self):
        self.l4 = Label(self.frame, text = "ENTER NO. OF COURSE OBJECTIVES", font=('Helvatical bold',12)).grid(row = 12, column = 0)
        self.e4 = Frame(self.frame, highlightbackground = self.mycolor2, highlightthickness = 1, bd=0)
        self.e4.grid(row = self.value, column = 1)
        self.entry3 = Entry(self.e4, width= 40, font=('Helvatical bold',12))
        self.entry3.pack()
        Label(self.frame, text = " ").grid(row = 13, column = 0)
        self.button_border = Frame(self.frame, highlightbackground = self.mycolor2, highlightthickness = 1, bd=0)
        self.button_border.grid(row = self.value + 2, column = 1)
        self.button1 = Button(self.button_border, text = "ENTER", font=('Helvatical bold',12), command=lambda:self.putColumns(self.entry3.get()), borderwidth = 0, fg = 'black', bg = 'white', padx = '20px')
        self.button1.pack()
        Label(self.frame, text = " ").grid(row = 14, column = 0)
        
    #function to create Next and Quit buttons   
    def createNextQuit(self):
        self.button_border5 = Frame(self.frame, highlightbackground = self.mycolor2, highlightthickness = 1, bd=0)
        self.button_border5.grid(row = 25, column = 1,sticky='e')
        self.button5 = Button(self.button_border5, text = "NEXT", command = self.disableFrame, font=('Helvatical bold',12), borderwidth = 0, fg = 'black', bg = 'white', padx = '20px')
        self.button5.pack()
        self.button_border6 = Frame(self.frame, highlightbackground = self.mycolor2, highlightthickness = 1, bd=0)
        self.button_border6.grid(row = 25, column = 1,sticky='w')
        self.button6 = Button(self.button_border6, text = "QUIT", command = root.destroy, font=('Helvatical bold',12), borderwidth = 0, fg = 'black', bg = 'white', padx = '20px')
        self.button6.pack()
        
    #constructor 
    def __init__(self, root):
        self.frame = LabelFrame(root, text = 'ENTER SUBJECT DETAILS',font=('Helvatical bold',12), padx=10, pady=10)
        self.frame.pack(padx=10,pady=10)
        self.createSubCode()
        self.createSubName()
        self.createCourseOutcomes()
        self.createCourseObjectives()
        self.createNextQuit()

#function to create new object        
def newFrame():
    b = window(root)

# window objects and technicals
root = Tk()     
root.title('QPMaker')
a = window(root)

root.mainloop()