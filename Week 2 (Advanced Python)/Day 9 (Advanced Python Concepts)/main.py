#List comprehensions

# list_var = [1,2,3,4,5] #static way of creating a list 

# odd_number = [i for i in range(1, 100, 2)] #creating list using list comprehension
# print(odd_number)

# even_number = [i for i in range(1, 100) if i%2 == 0] # using conditions in list comprehension
# print(even_number)

# #task 1
# a = [1,2,3,4,5]
# # b = [i**2 for i in a] #using list comprehesion 

# b=[]
# for num in a:
#     b.append(num**2) #using ** gives us power of variable

# print(b)

# #task 2
# number = [num**2 if num%2==0 else num ** 3 for num in range(1, 100)] # list comprehension using if and else condition (if even square else cube) 
# print(number)

#Generator Expression
'''
    -special type of function that return mutiple value for multiple different instances using yeild
    - don't store in memory , so memory effiecient than using functions
    -syntax:
        def function_name():
            yield statement
'''

# #Simple generator:
# def simple_generator():
#     yield 'a'
#     yield 'b'
#     yield 'c'

# #Approach 1 for getting result from generator
# for item in simple_generator():
#     print(item)

# #Approach 2
# print("**" * 30)
# x = simple_generator()
# print(next(x))
# print(next(x))
# print(next(x))

# print(next(x))

# sq_generator = (i**2 for i in range(1,10)) # Create a generator not a tuple
# print(sq_generator)
# print(list(sq_generator))

#task 3
even_generator = (num for num in range(1, 11) if num%2 ==0)
while True:
    try:
        user_input = input("Do you want to continue, type next to print next generator value :")
        if user_input == 'next':
            print(next(even_generator))
        else :
            print(even_generator)
    except Exception as e:
        print(f"The generator is completely executed {e}")
        break
