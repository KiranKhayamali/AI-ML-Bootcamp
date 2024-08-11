# #List
# list_var = [1, "kiran", 1.3]

# print(list_var, type(list_var))
# print("**" * 30)

# #interating over list using range
# for i in range(0, len(list_var)):
#     print(list_var[i])

# #iterating over list directly using element
# print("**" * 30)
# for list_element in list_var:
#     print(list_element)

# #iterating over list using enumerate using both index and element
# print("**" * 30)
# for list_index, list_element in enumerate(list_var):
#     print(f"{list_element} is at {list_index}")

# print("**" * 30)

# #Task 9
# num = [1,2,3,4,5,6,7,8,9,10]
# for even_num in num:
#     if even_num % 2 ==0:
#         print(even_num)

# print("**" *30)

# #How to add element in a list
# new_list = []
# print(new_list , len(new_list))

# # #staticly adding
# # new_list = [1]
# # print(new_list , len(new_list))

# #dynamic adding 
# for i in range(1, 9):
#     new_list.append(i)
    
# print(new_list , len(new_list))

# print("**" *30)

# #Task 10
# even_list = []
# for num in range(1, 101):
#     if num%2 == 0 :
#         even_list.append(num)

# print(even_list)

# #slicing the list
# list_var = [1,2,3,4,5,6,7,8,9]
# print(list_var[1:]) #slices list from the 2nd element
# print(list_var[1:4]) #slices list from 2nd element to 5th element

# #removing element from list
# list_var = [1,2,3,4,5,6,7,8,9]
# print(f"Original list: {list_var}")

# print(f"poping 3rd element from list : {list_var.pop(2)}")
# print(f"poping 6th element : {list_var.pop(4)}")
# print(f"poping 6th element : {list_var.pop(6)}")

# #task 11 : create a list of number 1-100 , then remove the odd number
# even_list = []
# for i in range(1, 101):
#     even_list.append(i)

# for index, num in enumerate(even_list):
#     if num %2 != 0:
#         even_list.pop(index)

# print(even_list)


# #Dictionary
# dict_val = {
#     'key1' : 1,
#     'key2' : "kiran", 
#     'key3' : [10, 20, 30, 40, 50]
# }

# print(dict_val['key3'])
# print(dict_val.keys())
# print(dict_val.values())

# list_keys = ['apple', 'ball', 'cat']
# list_values = ['red color fruit', 'something that is used to play', 'type of pet']

# dict1 = dict(zip(list_keys, list_values))
# print(dict1)

#Task 12
list_ques = []
list_ans = []
while True:
    user_ques = input("Enter question :")
    user_ans = input("Enter answer of the question :")
    user_input = input("DO you to continue?    :")
    list_ques.append(user_ques)
    list_ans.append(user_ans)
    if user_input == "N":
        break

question = dict(zip(list_ques, list_ans))

print(question)