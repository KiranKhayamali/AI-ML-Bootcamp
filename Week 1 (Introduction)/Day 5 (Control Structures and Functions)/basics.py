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

#Task 1
# username = input("Enter Username:")
# pasword = input("Enter Password:")

# if (username.lower() == "kiran") and (pasword == "password"):
#     print(f"Welcome {username}!")
# else:
#     print("Call 911")

#Task 2
#using dictionary and loop
# score = 0
# question = {
#     "What is captial of Nepal?": "kathmandu",
#     "What is the national bird of Nepal?" : "daphe",
#     "What is the tallest mountain of the world?": "everest",
#     "What is the deepest valley of the world?": "arun valley",
#     "Who is the prime minister of nepal?": "kp oli"
# }

# for ques, ans in question.items():
#     print(ques)
#     answer = input("Enter your answer:")
#     if (answer.lower()==ans):
#         score +=1
#     else:
#         print(f"Game Over! {score} of 5")
#         break

# print(f"Game Over! {score} of 5")

#using nested loop
# score = 0
# print("What is captial of Nepal?")
# if (input("Answer:").lower() == "kathmandu"):
#     score +=1
#     print("What is the national bird of Nepal?")
#     if (input("Answer:").lower() == "daphe"):
#         score +=1
#         print("What is the tallest mountain of the world?")
#         if (input("Answer:").lower() == "everest"):
#             score +=1
#             print("What is the deepest valley of the world?")
#             if (input("Answer:").lower() == "arun valley"):
#                 score +=1
#                 print("Who is the prime minister of nepal?")
#                 if (input("Answer:").lower() == "kp oli"):
#                     score +=1
#                     print(f"Game Over! {score} of 5")
#                 else:
#                     print(f"Game Over! {score} of 5")
#             else:
#                 print(f"Game Over! {score} of 5")
#         else:
#             print(f"Game Over! {score} of 5")
#     else:
#         print(f"Game Over! {score} of 5")
# else:
#     print(f"Game Over! {score} of 5")


#Loops
'''
    For loop is used in static data looping or data known vako bela
    While loop is used in dynamic data looping or data is unknown vako bela
'''

# for odd_number in range(1,100,2):
#     print(odd_number)

# for number in range(1,100):
#     if (number%2!=0):
#         print(number)

# #Task 4
# while True:
#     user_input = int(input("Enter Input:"))
#     if (user_input%5 == 0):
#         break

#Function

# def even_number_checker(x):
#     if (x%2 == 0):
#         print(f"{x} is even number.")
#     else:
#         print(f"{x} is odd number.")

# even_number_checker(9)
# even_number_checker(3)
# even_number_checker(2)
# even_number_checker(0)

# #task5
# def multiple_of_ten(x):
#     if (x%10 ==0):
#         print(f"{x} is multiple of 10.")
#     else:
#         print(f"{x} is not multiple of 10.")

# multiple_of_ten(100)
# multiple_of_ten(69)
# multiple_of_ten(40)

def even_odd_checker(x):
    if(x%2 == 0):
        return ("Even Number.", x)
    else:
        return ("Odd Number.", x)

output = even_odd_checker(9)
print(output)
