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
score = 0
print("What is captial of Nepal?")
if (input("Answer:").lower() == "kathmandu"):
    score +=1
    print("What is the national bird of Nepal?")
    if (input("Answer:").lower() == "daphe"):
        score +=1
        print("What is the tallest mountain of the world?")
        if (input("Answer:").lower() == "everest"):
            score +=1
            print("What is the deepest valley of the world?")
            if (input("Answer:").lower() == "arun valley"):
                score +=1
                print("Who is the prime minister of nepal?")
                if (input("Answer:").lower() == "kp oli"):
                    score +=1
                    print(f"Game Over! {score} of 5")
                else:
                    print(f"Game Over! {score} of 5")
            else:
                print(f"Game Over! {score} of 5")
        else:
            print(f"Game Over! {score} of 5")
    else:
        print(f"Game Over! {score} of 5")
else:
    print(f"Game Over! {score} of 5")