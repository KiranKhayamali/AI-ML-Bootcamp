#Map, Filter and Reduce 
'''
    - map take functions and collection of data to iterate all the element one by one
    - map can also use to map out 2 different parameter from 2 different collection over the function 
'''

list_of_numbers = [1,2,3,4,5,6,7,8,9,10]
output_of_map = list(map(lambda x : x **2 , list_of_numbers))
print(output_of_map)

def add_square(x,y):
    return x**2 +y**2

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
output_of_map_2 = list(map(add_square, list1, list2))
print(output_of_map_2)
