name = input("Enter your full name:")

spaceLoc = name.index(" ")

#print(spaceLoc)

sName = (name[spaceLoc+1:])

fName = (name[:spaceLoc])

print(fName)

print(sName)

