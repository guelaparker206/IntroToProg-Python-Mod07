# ------------------------------------------------- #
# Title: Pickling
# Description:  Pickle function
# ChangeLog: (Who, When, What)
# GuelaP,5.29.2022 Create script
# ------------------------------------------------- #

# Data -------------------------------------------- #
task_str = '' #Declare variable as string
priority_str = '' #Declare variable as string

# Processing -------------------------------------- #
import pickle  # This imports code from another code file
task_str = str(input("Enter a task: "))
priority_str = str(input("Enter the priority: "))
data_lst = [task_str, priority_str]

# Store the data with the pickle.dump method
objFile = open("Pickle.dat", "ab")
pickle.dump(data_lst, objFile)
objFile.close()

# Read the data back with the pickle.load method
objFile = open("Pickle.dat", "rb")
objFileData = pickle.load(objFile)
objFile.close()

print(objFileData)
