count = 99
while count > 0:
    if count >= 2:
        print(str(count) + " bottles of beer on the wall, " + str(count) + " bottles of beer.")
        print("Take one down and pass it around, " + str(count - 1) + " bottles of beer on the wall.")
    else:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    count = count - 1
