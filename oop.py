class Pet:
    vet_name = "Happy Tails Veterinary Clinic"

def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

def get_owner_first_name(self):
        return self.__owner_first_name

def get_owner_last_name(self):
        return self.__owner_last_name

def get_pet_id(self):
        return self.__pet_id

def get_pet_name(self):
        return self.__pet_name

def get_pet_type(self):
        return self.__pet_type

def set_owner_first_name(self, value):
        self.__owner_first_name = value

def set_owner_last_name(self, value):
        self.__owner_last_name = value

def set_pet_id(self, value):
        self.__pet_id = value

def set_pet_name(self, value):
        self.__pet_name = value

def set_pet_type(self, value):
        self.__pet_type = value

def display_pet_info(self):
        print("Owner:", self.__owner_first_name, self.__owner_last_name)
        print("Pet ID:", self.__pet_id)
        print("Pet Name:", self.__pet_name)
        print("Pet Type:", self.__pet_type)
        print("Veterinary Office:", Pet.vet_name)
        print()

def check_property(pet, property_name):
    print(hasattr(pet, property_name))

def main():
    pet1 = Pet("John", "Smith", "001", "Buddy")
    pet2 = Pet("Sara", "Miller", "002", "Whiskers", "Cat")
    pet3 = Pet("Tom", "Brown", "003", "Goldie", "Fish")

    pet2.set_pet_name("Mr. Whiskers")

    pet1.display_pet_info()
    pet2.display_pet_info()

    check_property(pet1, "_Pet__pet_name")
    check_property(pet2, "_Pet__pet_age")
    check_property(pet3, "_Pet__pet_type")

main()