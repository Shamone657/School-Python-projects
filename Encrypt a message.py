word = input("Type a word that is decrypted\n")

key = int(input("Type the key that was applied\n"))

for x in range(len(word)):
    
    ascii = ord(word[x])
    
    ew = (chr(ascii + key))
    
    print("Encrypted word is ", ew,)