#Map, Filter and Reduce 
'''
    - map take functions and collection of data to iterate all the element one by one
    - map can also use to map out 2 different parameter from 2 different collection over the function 
'''

# list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
# output_of_map = list(map(lambda x : x **2 , list_of_numbers))
# print(output_of_map)

# def add_square(x,y):
#     return x**2 +y**2

# list1 = [1,2,3,4,5]
# list2 = [6,7,8,9,10]
# output_of_map_2 = list(map(add_square, list1, list2))
# print(output_of_map_2)

# #task 1
# user_input = int(input("Enter the number of numbers:"))
# list1 = [int(input("Enter a list of number 1 :") ) for num in range(user_input) ]
# list2 = [int(input("Enter a list of number 2 :")) for num in range(user_input)]

# # add_two_num = list(map(lambda x, y: [x+y] if x+y ==10 else '' , list1, list2))
# # output = [str(num[0]) + str(num[1]) for num in add_two_num if num != '']

# # print(output)

# def is_10(x, y):
#     if x+y ==10:
#         return str(x) + str(y)
# output = list(map(is_10 , list1, list2))
# print(output)

# #filter function
# num = [i for i in range(0, 10)]
# evens = list(filter(lambda x : x%2 ==0 , num))
# print(evens)

# #task 2
# alist = ['apple', 'ball', 'cat', 'dog', 'elephent']
# output_list = list(filter(lambda x : len(x) >=1, alist))
# print(output_list)

#reduce function
'''
    -it runs in culmulative ways
    - reduce from left to right 
    -eg :[1,2,3,4] mult->
        [mult(1,2) , 3, 4]
        [mult(2,3), 4]
        [mult(6,4)]
        24

'''
from functools import reduce

# num = [i for i in range(1, 6)]
# output = reduce (lambda x, y: x*y , num)
# print(output)

# #Task 3
# user_input = int(input("Enter the number of numbers:"))
# user_list = [int(input(f"Enter a list of number {1+num} :") ) for num in range(user_input) ]

# square_and_add_4 = list(map(lambda x: x**2+4 , user_list))
# print(f"The list after squaring and adding by 4 is {square_and_add_4}")
# transition_list = list(filter(lambda y : y%5==0 , square_and_add_4))
# print(f"The list after filtering the list that is divisible by 5 is {transition_list}")
# total_sum = reduce(lambda x , y: x +y , transition_list)
# print(total_sum)


#Decorators
'''
    - decorators are special function that take in other function as parameter
    - decorators are understood by by the code editors with @
'''
def smart_conversion(func):
    def converter(x, y):
        return func(int(x), int(y))
    return converter
    
@smart_conversion
def division(x,y):
    return x/y

@smart_conversion
def addition(x,y):
    return x + y

print(addition('8', '5'))
print(division('9', '3'))