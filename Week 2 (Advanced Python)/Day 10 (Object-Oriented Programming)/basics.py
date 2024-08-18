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

class Animal:
    def what_sound_does_it_make(self, flag):
        if flag.lower() == 'bark':
            print(f"Hey Its a dog!!!")
        elif flag.lower() == 'meow':
            print("Hey Its a cat!!!")
        else:
            print("Its a human")

species_animal1 = Animal()
species_animal1.what_sound_does_it_make('bark')

species_animal2 = Animal()
species_animal2.what_sound_does_it_make('meow')

species_animal3 = Animal()
species_animal3.what_sound_does_it_make('talks')