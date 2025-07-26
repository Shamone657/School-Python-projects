item_n = ["Apple", "Banana", "Milk", "Water"] # items

item_q = [50, 50, 50, 50] #quantity

item_p = [0.5, 0.4, 1, 0.75] #prices

m = 1000 #money

print("€",m," \n Select an option: \n 1) View your items \n 2) Add a new item \n 3) Add to the stock \n 4) Remove item \n 5) Check an item \n 6) Buy an item \n 7) Exit")

x = input(":")

while (x != 7):

    if x in ["1", "view", "view items"]:
        
        print("--------------------------------------------------------") #divider
        
        for i in range (len(item_n)):
            
            print(f"{i}. {item_n[i]}, {item_q[i]}, €{item_p[i]}")
        
        print("--------------------------------------------------------") #divider
        
        x = 0
        
    elif x in ["2", "add", "add item"]:
        
        print("--------------------------------------------------------")
        
        i = input("Enter a new item: \n")
        
        q = input("Enter the quantity of the new item: \n")
        
        p = input("Enter the price for the new item: \n")
        
        item_n.append(i)
        
        item_q.append(q)
        
        item_p.append(p)
        
        print("--------------------------------------------------------")
        
        x = 0
        
    elif x in ["3", "add-stock", "stock"]:
        
        print("--------------------------------------------------------")
        
        for item in item_n:
            
            print(item)
        
        ist = input("Enter what item you want you want to change the stock with \n")
        
        ist = ist.capitalize()
        
        index = item_n.index(ist)
        
        item_q[index] = float(input("What will be the new stock of the item? \n"))
            
        x = 0
        
        print("--------------------------------------------------------")
        
    elif x in ["4", "remove", "remove-item"]:
        
        print("--------------------------------------------------------")
        
        for item in item_n:
            
            print(item)
            
        ist = input("Enter what item you want to delete \n")
        
        ist = ist.capitalize()
        
        index = item_n.index(ist)
        
        item_n = item_n[:index] + item_n[index + 1:]
        
        item_q = item_q[:index] + item_q[index + 1:]
        
        item_p = item_p[:index] + item_p[index + 1:]
        
        print("--------------------------------------------------------")
        
        x = 0
        
    elif x in ["5", "check", "check-stock"]:
        
        print("--------------------------------------------------------")
        
        ist = input("What item do you want to check if its in stock? \n")
        
        ist = ist.capitalize()
        
        index = item_n.index(ist)
        
        if item_q[index] > 0:
            
            print(ist, "is in stock!")
            
        else:
            
            print(ist, "is not in stock")
            
        print("--------------------------------------------------------")
            
        x = 0
        
    elif x in ["6", "buy", "buy-item"]:
        
        print("--------------------------------------------------------")
        
        for i in range (len(item_n)):
            
            print(f"{i}. {item_n[i]}, {item_q[i]}, €{item_p[i]}")
            
        it = input("What item would you like to buy? \n")
        
        it = it.capitalize()
            
        qu = int(input("How many items would you like to buy? \n"))
        
        index = item_n.index(it)
        
        p = item_p[index] * qu
        
        m = m - p
        
        item_q = item_q[index] - qu
        
        print("--------------------------------------------------------")
        
        x = 0
        
    else:
        
        print("Invalid choice")
        
    print("€",m," \n Select an option: \n 1) View your items \n 2) Add a new item \n 3) Add to the stock \n 4) Remove item \n 5) Check an item \n 6) Buy an item \n 7) Exit")

    x = input(":")
    
print("Ending...")