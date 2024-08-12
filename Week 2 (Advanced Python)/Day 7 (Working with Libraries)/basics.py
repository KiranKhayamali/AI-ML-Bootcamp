import pandas as pd 

'''
Pandas library:
    - pandas is equivalent to SQL for python, SQL already exists for python but pandas is more suitable for AI work
    - work on table, read table, modify table, save table and everything related to table
    - 
'''

dict_var = {
    'student' : ['aadim', 'aashish', 'anish', 'nimesh'],
    'marks' : [29, 32, 25, 27]
}

#pandas operations:
data_frame_var = pd.DataFrame(dict_var) #higher level of data abstraction convert dictionary into dataframe(table)
print("Before adding new column :")
print(data_frame_var)

#Adding new column
data_frame_var['social skils'] = [90, 80, 85, 95]
print("After adding new column :")
print(data_frame_var)

# #Removing column
# print("After removing a column :")
# data_frame_var = data_frame_var.drop(columns= ['marks'])
# print(data_frame_var)

#Looking for certain column
failed_student = data_frame_var.loc[data_frame_var['marks'] < 32]
print("Failed Students :")
print(failed_student)

#Saving dataframe to csv
data_frame_var.to_csv('data.csv', index=False)

#Loading form csv
new_dataframe = pd.read_csv('data.csv')
print("Loaded from csv :")
print(new_dataframe['student'])

#Iloc
print(new_dataframe.iloc[1]) #this is used to look up index 1 dataframe item

#loc
print(new_dataframe.loc[(new_dataframe['student'] == 'aadim') & (new_dataframe['marks'] <= 50)]) #this is used to look up item that fulfill both condition in dataframe

# #Task 1
# list_ques = []
# list_ans = []
# while True:
#     user_ques = input("Enter question: ")
#     user_ans = input("Enter answer of the question: ")
#     list_ques.append(user_ques)
#     list_ans.append(user_ans)
#     user_input = input("Do you want to continue? (Y/N): ")
#     if user_input.upper() == "N":
#         break

# # Create a DataFrame from the lists
# question_data_frame = pd.DataFrame({
#     'Question': list_ques,
#     'Answer': list_ans
# })

# print(question_data_frame)

# #Task 2 (getting question :what is the capital of nepal)
# print("**" * 30)
# print(question_data_frame.loc[(question_data_frame['Question'] == "what is the captial of nepal") & (question_data_frame['Answer'] == "ktm") ]) #for getting a row using condition

