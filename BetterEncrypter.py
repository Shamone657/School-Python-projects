word = input("Enter a sentence")

key = int(input("Enter a number"))

encrypted = ""

for x in word:
    
    encrypted += chr((ord(x) + key))
    
print(encrypted)