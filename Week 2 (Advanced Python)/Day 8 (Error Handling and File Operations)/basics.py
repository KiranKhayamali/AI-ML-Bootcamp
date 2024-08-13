'''
Exception handling:
    -sometime their might be some king of error in our code
    -Exception handling has mainly two part:
        try:
            code in try block (code trying to execute)
        except:
            if code fails rest of the part run here
'''

x = 0
y = 10
try:
    print(f"the divison by 0 {y/x}")
except Exception as e:
    print(f"Got error as {e}!!!")

