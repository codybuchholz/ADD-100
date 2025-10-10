print ("Please enter five different names. ")
names = []
for i in range(5):
    name = input(f"Enter name #{i + 1}: ")
    names.append(name) 
n = len(names)
for i in range(n - 1): 
    for x in range(n - i - 1):
        if names[x]> names[x + 1]:
            names[x], names[x + 1] = names[x + 1],  names[x]
print (names)
names.reverse()
print (names)