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
print(data_frame_var)