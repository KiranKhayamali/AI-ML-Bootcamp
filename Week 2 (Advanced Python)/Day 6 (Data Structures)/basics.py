#List
list_var = [1, "kiran", 1.3]

print(list_var, type(list_var))
print("**" * 30)

#interating over list using range
for i in range(0, len(list_var)):
    print(list_var[i])

#iterating over list directly using element
print("**" * 30)
for list_element in list_var:
    print(list_element)

#iterating over list using enumerate using both index and element
print("**" * 30)
for list_index, list_element in enumerate(list_var):
    print(f"{list_element} is at {list_index}")

print("**" * 30)
