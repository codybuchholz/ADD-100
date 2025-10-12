def custom_song(name, adverb, clothing_item, noun, item_that_makes_noise, plural_noun, object):
    print("\n Another One Bites the Dust Mad Lib\n ")
    print(f"{name} walks {adverb} down the street,")
    print(f"With the {clothing_item} pulled way down low.")
    print(f"Ain't no sound but the sound of {noun},")
    print(f"{plural_noun} ready to go.")
    print("Are you ready? Hey, are you ready for this?")
    print(f"Are you hanging on the edge of your {object}?")
    print(f"Out of the doorway, the {plural_noun} zip,")
    print(f"To the sound of the {item_that_makes_noise}, yeah!")

input_name = input("Enter a name: ")
input_adverb = input("Enter an adverb: ")
input_clothing_item = input("Enter a clothing item: ")
input_noun = input("Enter a noun: ")
input_item_that_makes_noise = input("Enter something that makes noise: ")
input_plural_noun = input("Enter a plural noun: ")
input_object = input("Enter an object: ")

custom_song(
    name=input_name,
    adverb=input_adverb,
    clothing_item=input_clothing_item,
    noun=input_noun,
    item_that_makes_noise=input_item_that_makes_noise,
    plural_noun=input_plural_noun,
    object=input_object
)