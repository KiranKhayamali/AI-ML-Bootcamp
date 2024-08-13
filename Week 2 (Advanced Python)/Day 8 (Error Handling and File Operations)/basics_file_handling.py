'''
All variable are stored in runtime memory during execution
These variable are volatile in nature 

To avoid deletion or to use these variable on long term we need to save these variable or state of variables somewhere permanently
'''

# user_name = input("Enter Username :")
# password = input("Enter Password :")
# print(user_name, password)
# print("**" * 30)

# #Writing in file
# with open('database.txt', 'w') as f:
#     f.writelines(user_name + ' : ' + password)

# #Reading a file
# with open('database.txt', 'r') as f:
#     from_file_output = f.readlines()

# print(from_file_output)

# #Append in file
# with open('database.txt', 'a') as f:
#     f.writelines(user_name + ' : ' + password)


#Task 2
'''
    1.Write note
    2. Read note

    if 1 is pressed pass to writing note and after complete store in file 
    if 2 is pressed present all note
'''
# def read_write_note(flag):
#     try:
#         if flag == 1:
#             note = input("Enter your note :")
#             with open('note.txt', 'a') as writenote:
#                 writenote.write(note + '\n')
#         elif flag == 2:
#             with open("note.txt", 'r') as readfile:
#                 whole_note = readfile.readlines()

#             print(whole_note) 
#         else :
#             print("Not enough function yet!!")
#     except Exception as e:
#         print(e)
    

# user_input = int(input("Enter 1 to write the note and 2 to read the note :"))
# read_write_note(user_input)

#JSON
import json 
to_save_dict = {
    'Student' : ['Aadim', 'Aashish', 'Anish', 'Nimesh'],
    'Marks' : [10 , 20, 30, 40]
}

with open('database_json.json', 'w') as f:
    json.dump(to_save_dict, f)

with open('database_json.json', 'r') as f:
    loaded_data = json.load(f)

print(loaded_data)