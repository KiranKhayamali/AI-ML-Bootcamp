'''
Class :
    -> Collection of function and variables, which can works on independently on its own.
    -> Example in real world scenario are animal, vehicles

Object :
    -> Instance of class (part of class that haw its own independent identity)
    -> Dog from animal can be an object of animal class, ferarri from vehicles
    -> Each object has its own set of attributes/features and also acts indifferently
    -> Dog has 4 legs(variable) and bark(function)
'''

# class Animal:
#     def what_sound_does_it_make(self, flag):
#         if flag.lower() == 'bark':
#             print(f"Hey Its a dog!!!")
#         elif flag.lower() == 'meow':
#             print("Hey Its a cat!!!")
#         else:
#             print("Its a human")

# species_animal1 = Animal()
# species_animal1.what_sound_does_it_make('bark')

# species_animal2 = Animal()
# species_animal2.what_sound_does_it_make('meow')

# species_animal3 = Animal()
# species_animal3.what_sound_does_it_make('talks')

# #Task 1
# class Calculator:
#     def add (self, num1, num2):
#         print(num1+ num2)
#     def sub (self, num1, num2):
#         print( num1- num2)
#     def mul(self, num1, num2):
#         print( num1*num2)
#     def div (self, num1, num2):
#         print( num1 / num2)
    
# calculate_1 = Calculator()
# calculate_1.add(38, 20)
    
# calculate_2 = Calculator()
# calculate_2.sub(38, 20)

# calculate_3 = Calculator()
# calculate_3.mul(39, 25)

    
# calculate_4 = Calculator()
# calculate_4.div(36, 4)

'''
Constructor:
    -> used during initalization, such that as soon as object is created it jumps to the constructor part
    -> syntax :
        def __init__(self):
            constructor_code()
'''

# class KBC:
#     def __init__(self, username):
#         print(f"Welcome to KBC for {username}")

# game_for_player1 = KBC("player1")
# game_for_player2 = KBC("player2")


'''
How does encapsulation and different instances works
'''

# class Animal:
#     def __init__(self, animal_name, animal_species, animal_age):
#         self.name = animal_name
#         self.species = animal_species
#         self.age = animal_age
#     def display(self):
#         print(f"The animal is {self.name} having species of {self.species} with age {self.age}")

# dog_animal = Animal('bob', 'german shephard', 5)
# cat = Animal ('kuro', 'black panther', 9)

# print("Accessing information from outside of the class:")
# print(dog_animal.name, dog_animal.species, dog_animal.age)
# print(cat.name, cat.species, cat.age)

# print("Accessing the information from inside the class:")
# dog_animal.display()
# cat.display()



'''
Task 2: 
    WAP that uses oop
    has class user
    when initalized it provides options: 
    1. Sign up 
    2. Sign in 

    if 1 is pressed it redirects to a method named Register_User
    this method takes in username, password and mobile number

    if 2 is pressed it redirects to a method name authentication
    this method checks input username and password with self.username
    and self.password 

    if match it redirects to another method named welcome_user

    welcome user method greets them,displays username and displays 
    their mobile number

    also this method gives 3 options. 
    1. enter note 
    2. Display notes
    3. exit 

    if 1 is pressed user can input a large note that is saved for that 
    object 

    if 2 is pressed display the note that was saved earlier 

    if 3 is pressed terminate 
'''
class User:
    def __init__(self):
        self.file = 'users.json'
        self.notes = []
        self.load_user()

    def welcome_user(self):
        print(f"Hello {self.username} to the program! \n {self.username} has mobile number : {self.number}")
        user_input = input("1. Enter Notes \n2. Display Notes \n3. Exit \n:")

    def register_user(self):
        self.username = input("Enter UserName :")
        self.password = input("Register a password :")
        self.number = input(f"Hey {self.username}! What is your mobile number :")

    def authenticate(self):
        username = input("Enter your username :")
        password = input("Enter your password :")
        if username == self.username and password == self.password:
            self.welcome_user()

    user_input = input(f"1. Sign up \n2.Sign up \n3.Exit \n:")
    if user_input == 1:
        register_user()
    elif user_input == 2:
        authenticate()
    elif user_input == 3:
        exit

user1 = User()