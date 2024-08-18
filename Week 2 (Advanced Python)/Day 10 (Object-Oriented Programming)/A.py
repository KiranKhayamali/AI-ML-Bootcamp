def add(a, b):
    return a +b
def sub (a,b):
    return a - b
def mul (a,b):
    return a *b
def div(a, b):
    return a /b

if __name__ =='__main__': #this is execute only if the A.py is executed
    print(f"Addition from A.py file : {add(4, 10)}")
    print(f"Subtraction from A.py file : {sub(19, 7)}")
    #so the above operation won't be happening when imported to another file to use