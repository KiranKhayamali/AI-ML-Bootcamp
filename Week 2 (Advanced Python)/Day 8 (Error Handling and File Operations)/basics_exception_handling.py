'''
Exception handling:
    -sometime their might be some king of error in our code
    -Exception handling has mainly two part:
        try:
            code in try block (code trying to execute)
        except:
            if code fails rest of the part run here
'''

# x = 0
# y = 10
# try:
#     print(f"the divison by 0 {y/x}")
# except Exception as e:
#     print(f"Got error as {e}!!!")

# import random
# a = random.randint(0,100)
# b = random.randint(0,100)
# print(f"The random a {a} and {b} is divided as {b/a}")

#task 1 
# start infinite loop get random numerator and denomerator
# and calculate total number of crashes 
# if total number of crashes is greater than equal to 100 , program terminates

#standard pratice 1 
#try to do everything using function

#standard pratice 2
# Use try excpet on each function

# import random

# crashes =0
# while True:
#     numerator = random.randint(0,100)
#     denomerator = random.randint(0,100)
#     try:
#         output = numerator / denomerator
#     except Exception as e:
#         crashes +=1
#         print("crashes :", crashes)
#         if crashes >= 100:
#             break

#try yourself or explore yourself