# print("hello world")

"""
x = int(input('Enter number 1:'))
y=int(input('Enter number 2:'))
print(f'add:{x+y}\nsub:{x-y}\nmult:{x*y}\ndiv:{x/y}')
"""

# WAP to take principal, tile and rate then calculate the simple interest
p = float(input('Enter principal:'))
t = int(input('Enter time: '))
r = float(input('Enter Rate: '))
SI=(p*t*r)/100
print(f"PRINCIPLE:RS.{p}\nTIME:{t} YEARS\nRATE:{r}%\nSIMPLE INTEREST:RS.{SI}")