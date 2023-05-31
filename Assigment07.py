# ------------------------------------- #
# Title: Assignment07 - Pickling and Error Handling
# Developer: CRichardson
# Date: 2023-05-28
# Change Log: (Who, When, What)
#  CRichardson, 2023-05-28, Initial Development
# Description: This is a script that experiments with Pickling and Error Handing within Python.
#              When Pickling the data is imported from another code file AppData.dat.
#              When Error Handling the use case was to ensure the Priority was input as an integer.
# ------------------------------------- #

import pickle  # Imports code from another code file

# Data -------------------------------------------- #
strAppData = 'AppData.dat'
lstToDo = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    """ Saves string data to a file

     :param data: (string) with data to save
     :param file_name: (string) with name of file
     :return: nothing
     """
    file = open(file_name, "ab")
    pickle.dump(list_of_data, file)
    file.close()

def read_data_from_file(file_name):
    """ Reads rows of data from a file into a list

        :param file_name: (string) with name of file
        :return: (list) with rows of data read from the file
        """
    file = open(file_name, "rb")
    list_of_data = pickle.load(file)
    file.close()
    return list_of_data

# Presentation ------------------------------------ #
# Request a Number, Task, and Priority from user, then store it in a list object
strTask = str(input("Enter a Task: ")).strip()
intPriorityNumber = str(input("Enter a Priority on a scale of 1 to 10: "))

try:
    intPriorityNumber = int(intPriorityNumber)
    print(intPriorityNumber)
# except ValueError:  # For Error Handling the Value Error is used to ensure the user inputs an integer
#     print("Please enter an integer")
except Exception as e:  # This is a catch-all for any other error that would occur at this step
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e.__doc__)
    print(e.__str__())

lstToDo = [strTask, intPriorityNumber]

save_data_to_file(strAppData, lstToDo)

print(read_data_from_file(strAppData))
