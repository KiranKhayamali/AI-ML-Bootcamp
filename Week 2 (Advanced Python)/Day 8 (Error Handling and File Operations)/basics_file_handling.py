'''
All variable are stored in runtime memory during execution
These variable are volatile in nature 

To avoid deletion or to use these variable on long term we need to save these variable or state of variables somewhere permanently
'''

user_name = input("Enter Username :")
password = input("Enter Password :")
print(user_name, password)
print("**" * 30)

#Writing in file
with open('database.txt', 'w') as f:
    f.write(user_name + ' : ' + password)
