#List comprehensions

# list_var = [1,2,3,4,5] #static way of creating a list 

# odd_number = [i for i in range(1, 100, 2)] #creating list using list comprehension
# print(odd_number)

#task 1
a = [1,2,3,4,5]
# b = [i**2 for i in a] #using list comprehesion 

b=[]
for num in a:
    b.append(num**2) #using ** gives us power of variable
print(b)
