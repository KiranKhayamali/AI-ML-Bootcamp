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

#Removing column
print("After removing a column :")
data_frame_var = data_frame_var.drop(columns= ['marks'])
print(data_frame_var)

