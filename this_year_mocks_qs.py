s = 0

l = 0

n = 0

w = 0

sen = input("Please enter a sentence:\n")

print(sen)

sen.lower()

print(sen.lower())

for char in sen:
    
    if char.lower() == "s":
        
        s += 1
        
    if char.isalpha():
        
        l += 1
        
    if char.isdigit():
        
        n += 1

in_word = False
        
for char in sen:
    
    if char.isspace():
        
        in_word = False
        
    elif not in_word:
        
        w += 1
        
        in_word = True
    
print("Number of s's are: ",s)
print("Number of l's are: ",l)
print("Number of digits are: ",n)
print("Number of words are: ",w)