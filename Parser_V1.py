"""

This file contains the class to parse the input worksheet into a dictionary
of panda dataframes.

Created and Reviewed by:


"""
import pandas as pd


class DataParser:
    """
    The DataParser class is the base class for all the data processing class.
    It contains the methods to parse the input worksheet into a dictionary of panda dataframes.

    """
    def __init__(self, workbook_address, worksheet_name):
        self.workbook_address = workbook_address
        self.worksheet_name = worksheet_name
        self.main_dataframe = pd.read_excel(self.workbook_address, sheet_name = self.worksheet_name)
        self.data_dict = {}
        self.type_of_questions = []

    def unique_type_finder(self):
        """
        This method finds the unique types of questions in the worksheet.

        :return type_of_questions: list of unique types of questions
        """
        self.type_of_questions = self.main_dataframe.TYPE.unique()
        return self.type_of_questions

    def data_dict_creator(self):
        """
        This method creates a dictionary of dataframes.

        :return data_dict: dictionary of dataframes
        """
        for question in self.type_of_questions:
            key = self.worksheet_name + '_' + question
            self.data_dict[key] = self.main_dataframe[self.main_dataframe['TYPE'] == question]
        return self.data_dict



class Organizer:
    """
    this class organizes the given workbook data into a easily accessible data
    
    """
    def __init__(self, workbook_address, worksheet_list):

        self.dict_list = []
        self.workbook_address = workbook_address
        self.worksheet_list = worksheet_list

    def collective_list_creator(self):
        for unit in self.worksheet_list:
            testobj = DataParser(self.workbook_address, unit)
            testobj.unique_type_finder()
            self.dict_list.append(testobj.data_dict_creator())

        return self.dict_list



if __name__ == "__main__":
    obj = Organizer("D:\\qpop\\docx_n_pdfs\\QuestionBank.xlsx", ['Unit1', 'Unit2'])
    # print(obj.collective_list_creator())
    out_list = obj.collective_list_creator()
    print(out_list[0]['Unit1_a'])


"""
the data dictionary is not working for multiple units.
empty dataframes are being created for the units

"""