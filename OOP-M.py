class Pet:
    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    #Get Kind
    def get_kind(self):
        return self.__kind

    def set_kind(self, kind):
        self.__kind = kind

    #Get breed
    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

    #Get name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def print_details(self):
        print(f"Kind: {self.__kind}, Breed: {self.__breed}, Name: {self.__name}")


#Pet instances
pet1 = Pet("Dog", "Labrador", "Buddy")
pet2 = Pet("Cat", "Siamese", "Whiskers")
pet3 = Pet("Bird", "Parrot", "Kiwi")

pet1.print_details()
pet2.print_details()
pet3.print_details()

print(Pet.__name__)  #Pet output

print(type(pet1))  


print(isinstance(pet2, Pet)) 