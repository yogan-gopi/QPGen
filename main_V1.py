from Selecthor_V1 import Selecthor
from QPClassesPARTA_V1 import *
from time import sleep
from answerFormat_V1 import *
from jsonArray_V1 import *
from rich.console import Console
from rich import print
from datetime import datetime
import os

console = Console()

address = os.getcwd() + "\\resrc\\DAA_QB.xlsx"
exam = "IA1"
question = "a"

date = datetime.today()



print("--------------------------------------------------------------------------------------------")
print("\n")
print("\t QPGen - Version 1.0 \n")
print("\t Question Paper Generator \n")
print("\t Developed by: \n")
print("\t yet to decide \n") 
print("\n")
print("--------------------------------------------------------------------------------------------\n")
 
while True: 
    print("\t 1. Enter\\Update the Subject Details\n")
    print("\t 2. Generate the Question Paper and Answer Key\n")
    print("\t 3. Exit\n")

    choice = int(input("\t Enter your choice: "))

    print("\n")
    print("--------------------------------------------------------------------------------------------\n")

    if choice == 1:
        with console.status("[bold green] Gathering data for the subjects...") as status:
            from jsondatagetter_V1 import *
            
            print("\n")
        console.log("[bold green] Data gathered successfully!")

    if choice == 2:
        print("\t Enter the subject code: \n")
        subject_code = input()
        subject_name = {
                "CS1001" :"Design and Analysis of Algorithms"
        }
        with console.status("[bold green]Generating Question Paper and Answer Key...", spinner = 'aesthetic') as status:
            select_obj = Selecthor(address, exam, question)
            select_obj.index_selector()
            sub_co_list, sub_co_no_list, sub_obj_list = getArray(subject_code)
            Engrave.header(exam=0,
                      examno= 2 ,
                      month= date.month,
                      year= date.year,
                      date= date.day,
                      subjcode= subject_code,
                      subjname= subject_name[subject_code],
                      branch= 0,
                      Set= 0,
                      marks= 0 ,
                      AcaYear= 2,
                      Sem= 4)
            Engrave.courseObjectives(sub_obj_list)
            Engrave.courseOutcomes(sub_co_no_list,
                                   sub_co_list)
            print(select_obj.q_a_list)
            print(select_obj.a_a_list)
            print(select_obj.co_a_list)
            print(select_obj.bt_a_list)
            print(select_obj.p_a_list)

            Engrave.partA(select_obj.q_a_list,
                          select_obj.co_a_list,
                          select_obj.bt_a_list,
                          select_obj.p_a_list)
            Create()

            answerKey(exam=0,
                      examno= 2 ,
                      month= date.month,
                      year= date.year,
                      date= date.day,
                      subjcode= subject_code,
                      subjname= subject_name[subject_code],
                      branch= 0,
                      Set= 0,
                      marks= 0 ,
                      AcaYear= 2,
                      Sem= 4,
                      a_list= select_obj.a_a_list)
        console.log("[bold green]Question Paper and Answer Key generated successfully!")




    if choice == 3:
        with console.status("[bold green]Exiting...") as status:
            sleep(1)
            print("\n")
            break
        console.log("[bold green]Exited successfully!")
        sleep(0.1)

exit()