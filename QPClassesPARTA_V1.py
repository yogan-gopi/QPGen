from QPtemplatePARTA_V1 import *

class Header:
    #exam type - Internal Assessment, Model Exam, etc
    exam=["Internal Assessment","Model Exam"]
    MONTH=[0,"January","February","March","April","May","June","July","August","September","October","November","December"]
    branch=["CSE","EEE","ECE","IT","MECH","MCT","CSBS","AIDS","BME","CVL","S&H"]
    Set=["A","B"]
    marks=["50 Marks","100 Marks"]
    time=["1.30 hours","3 hours"]
    AcaYear=[0,"I","II","III","IV"]
    Sem=[0,"I","II","III","IV","V","VI","VII","VIII"]
    H=[]
    def __init__(self,exam,examno,month,year,date,subjcode,subjname,branch,Set,marks,AcaYear,Sem):
        self.H.append(self.exam[exam])#int 0-1
        self.H.append(examno) 
        self.H.append(self.MONTH[month])#int val
        self.H.append(year)#int val
        self.H.append(str(date)+"/"+str(month)+"/"+str(year))
        self.H.append(subjcode)#str
        self.H.append(subjname)#str
        self.H.append(self.branch[branch])#int 0 - 10
        self.H.append(self.Set[Set]) #int 0-1
        self.H.append(self.marks[marks]) #int 0-1
        self.H.append(self.time[marks])
        self.H.append(self.AcaYear[AcaYear]) #int 1-4
        self.H.append(self.Sem[Sem]) # int 1-8
   

class CourseObjectives:
    #only cobj column
    CObj=[]
    
    def __init__(self,C):
         for i in C:
             self.CObj.append(i)
    
    

class CourseOutcomes:
    #cout no and cout column list
    COut=[]
    def __init__(self,cout_code,cout):
        self.COut.append(cout_code)
        self.COut.append(cout)
    

class PartA:
    partA=[]
    def __init__(self,Qns,CO,BT_Level,Univ_QP_Reference):
        self.partA.append(Qns)
        self.partA.append(CO)
        self.partA.append(BT_Level)
        self.partA.append(Univ_QP_Reference)

class Engrave:

   def header(exam,examno,month,year,date,subjcode,subjname,branch,Set,marks,AcaYear,Sem) :
    Header(exam,examno,month,year,date,subjcode,subjname,branch,Set,marks,AcaYear,Sem)

#Course Objectives-----------------------------------------------------------------------------------------------
   def courseObjectives(c):
    CourseObjectives(c)

#Course outcomes-------------------------------------------------------------------------------------------------
   def courseOutcomes(cout_code,cout):
    CourseOutcomes(cout_code,cout)

#Part A----------------------------------------------------------------------------------------------------------
   def partA(Qns,CO,BT_Level,Univ_QP_Reference):
    PartA(Qns,CO,BT_Level,Univ_QP_Reference)

class Create: 
    docx=[]
    def __init__(self): #to create template
       Data(Header.H,CourseObjectives.CObj,CourseOutcomes.COut,PartA.partA)
      