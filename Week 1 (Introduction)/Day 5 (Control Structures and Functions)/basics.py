'''
Conditional Statement 
    syntax:
        if(condition):
            satisfied_function()
        elif(condition):
            elif_satisfied_function()
        else:
            Unsatisfied_function()

'''

# x = 9
# if (x==0):
#     print(f"{x} is zero number.")
# elif (x%2==0):
#     print(f"{x} is an even number.")
# else:
#     print(f"{x} is an odd number.")

username = input("Enter Username:")
pasword = input("Enter Password:")

if (username.lower() == "kiran") and (pasword == "password"):
    print(f"Welcome {username}!")
else:
    print("Call 911")