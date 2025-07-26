word = input("Enter a word\n")

key = int(input("Enter a number\n"))

for x in range(len(word)):
    
    ascii = ord(word[x])
    
    ew = chr(ascii + key)
    
    print(ew)