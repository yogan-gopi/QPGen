from Parser_V1 import Organizer
import random
import pandas as pd


class Selecthor:
    """
    the input for the constructor contains as usual the workbook address
    and the other inputs are :
    the exam type

    the q_type_list

    """
    def __init__(self, workbook_address, exam_type, q_type):
        self.workbook_address = workbook_address
        self.exam_type = exam_type
        self.q_type = q_type
        self.list_cases = {
            "IA1":['Unit1'],
            "IA2":['Unit2','Unit3'],
            "IA3":['Unit1','Unit2','Unit3','Unit4','Unit5']
        }
        self.unit_list = self.list_cases[self.exam_type]
        org_object = Organizer(self.workbook_address, self.unit_list)
        self.df_list = org_object.collective_list_creator()
        self.q_a_list = []
        self.a_a_list = []
        self.p_a_list = []
        self.co_a_list = []
        self.bt_a_list = []    
        self.n = [] 
 
        


    def index_selector(self):


        if self.exam_type == "IA1":
            
            df = self.df_list[0]['Unit1_a']
            df = df.sample(n=5)
            # print(df)
            self.q_a_list = df['QUESTION'].reset_index(drop=True)
            self.a_a_list = df['ANSWERS'].reset_index(drop=True)
            self.p_a_list = df['PAPER'].reset_index(drop=True)
            self.co_a_list = df['CO'].reset_index(drop=True)
            self.bt_a_list = df['BT'].reset_index(drop=True)


        elif self.exam_type == "IA2":
            df_1 = self.df_list[0]['Unit2_a']
            df_2 = self.df_list[1]['Unit3_a']
            n = random.choice([3,2])
            df_1 = df_1.sample(n=n)
            # print(df_1)
            df_2 = df_2.sample(n=5-n)
            # print(df_2)
            df = pd.concat([df_1,df_2]) 
            # print(df)
            self.q_a_list = df['QUESTION'].reset_index(drop=True)
            self.a_a_list = df['ANSWERS'].reset_index(drop=True)
            self.p_a_list = df['PAPER'].reset_index(drop=True)
            self.co_a_list = df['CO'].reset_index(drop=True)
            self.bt_a_list = df['BT'].reset_index(drop=True)


        elif self.exam_type == "IA3":
            df_1 = self.df_list[0]['Unit1_a'].sample(n=2)
            df_2 = self.df_list[1]['Unit2_a'].sample(n=2)
            df_3 = self.df_list[2]['Unit3_a'].sample(n=2)
            df_4 = self.df_list[3]['Unit4_a'].sample(n=2)
            df_5 = self.df_list[4]['Unit5_a'].sample(n=2)
            df = pd.concat([df_1,df_2,df_3,df_4,df_5])
            # print(df)
            self.q_a_list = df['QUESTION'].reset_index(drop=True)
            self.a_a_list = df['ANSWERS'].reset_index(drop=True)
            self.p_a_list = df['PAPER'].reset_index(drop=True)
            self.co_a_list = df['CO'].reset_index(drop=True)
            self.bt_a_list = df['BT'].reset_index(drop=True)




# if __name__ == "__main__":
#     obj = Selecthor("D:\\qpop\\docx_n_pdfs\\QuestionBank.xlsx", "IA3", "a")
#     # obj.n_definer()
#     obj.index_selector()
#     print(obj.q_list)
#     print(obj.a_list)
#     print(obj.p_list)
#     print(obj.co_list)
#     print(obj.bt_list)


"""
lets make it work for now and later add the easy med hard and the importance criteria

"""