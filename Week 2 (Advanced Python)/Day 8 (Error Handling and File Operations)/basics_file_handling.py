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
  
#Task 3
'''Task 3: WAP that first gives 2 options: 
1. Sign up 
2. Sign in 

when 1 is pressed user needs to provide following information 
1. Username, 2. Password, 3. Mobile number 
All this information is saved in a file everytime a new user signs up the same file is updated 
(hint Append over the same file)

when 2 is pressed 
User needs to provide username and password 
this username and password is checked with username and password in the database
if matched: 
welcome to the device and show their phone number 
else: 
terminate the program saying incorrect credentials 


Do it using json files, save everything to json and load from json 
'''
# #Using Text file as data storage
# def register(flag):
#     if flag ==1:
#         username = input("Enter username :")
#         password = input("Enter password :")
#         mobile_number = int(input("Enter Mobile number :"))
#         with open('account.txt', 'a') as f:
#             f.write(username +" : " + password + " : " + str(mobile_number) +"\n")

#     elif flag == 2:
#         user_username = input("Enter your username : ")
#         user_password = input("Enter your password : ")
#         credentials_found = False
#         with open('account.txt', 'r') as f: 
#             file_acc = f.readlines()
#             for i in range(len(file_acc)):
#                 file_acc_new = file_acc[i].split(' : ')
#                 if (user_username == file_acc_new[0]) and (user_password == file_acc_new[1]):
#                     print(f"Welcome to the device! The mobile number of user {user_username} is {file_acc_new[2]}")
#                     credentials_found = True
#                     break
#             if not credentials_found:
#                 print("Wrong username and/or password!!")

# user_input = int(input("Enter 1 to sign up and 2 to sign in :"))
# register(user_input)

#Using JSON as data storage
import json
import os
def register(flag):
    # Ensure the file exists before trying to read it
    if not os.path.exists('account.json'):
        with open('account.json', 'w') as f:
            json.dump([], f)  # Initialize with an empty list
    
    if flag ==1:
        username = input("Enter username :")
        password = input("Enter password :")
        mobile_number = int(input("Enter Mobile number :"))
        user_details={
            "Username" : username,
            "Password" : password,
            "Mobile Number" : mobile_number
        }

        # Load existing users, if any
        with open('account.json', 'r') as f:
            try:
                users = json.load(f)
            except json.JSONDecodeError:
                users = []  # Handle case where the file is empty or invalid
        
        # Append the new user details to the list of users
        users.append(user_details)
        
        # Write the updated list back to the file
        with open('account.json', 'w') as f:
            json.dump(users, f, indent=4)
        print("User registered successfully!")

    elif flag == 2:
        user_username = input("Enter your username : ")
        user_password = input("Enter your password : ")
        credentials_found = False
        with open('account.json', 'r') as f:
            try:
                users = json.load(f)
                for user in users:
                    if (user_username == user["Username"]) and (user_password ==user["Password"]):
                        print(f"Welcome to the device! The mobile number of user {user_username} is {user["Mobile Number"]}")
                        credentials_found = True
                        break
                if not credentials_found:
                    print("Wrong username and/or password!!")
            except json.JSONDecodeError:
                users = [] # Handle case where the file is empty or invalid

user_input = int(input("Enter 1 to sign up and 2 to sign in :"))
register(user_input)


# #JSON
# import json 
# to_save_dict = {
#     'Student' : ['Aadim', 'Aashish', 'Anish', 'Nimesh'],
#     'Marks' : [10 , 20, 30, 40]
# }

# with open('database_json.json', 'w') as f:
#     json.dump(to_save_dict, f)

# with open('database_json.json', 'r') as f:
#     loaded_data = json.load(f)

# print(loaded_data)