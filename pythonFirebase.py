from firebase import firebase
import time

DB = firebase.FirebaseApplication("https://cs2025-f556f-default-rtdb.europe-west1.firebasedatabase.app/", None)

allRecords = DB.get('/patients/',None)

def inputRecords():
    fn = input("What is your first name? \n")
    ln = input("What is your last name? \n")
    age = input("What is your age? \n")

    record = {
        "firstName" : fn,
        "lastName" : ln,
        "age" : age
        }
    
    DB.post('/patients/',record)

def displayRecords():
    for i in allRecords:
        print(allRecords[i]['firstName'], end="\t")
        print(allRecords[i]['lastName'], end="\t")
        print(allRecords[i]['age'])


print("Option 1 - Display Names")
print("Option 2 - Display all information")
print("Option 3 - Enter Data")
print("Option 4 - Exit")

option = int(input("Select option 1 - 4: "))

while option != 4:

    allRecords = DB.get('/patients/',None)
    
    if option == 1:
        for i in allRecords:
            print(allRecords[i]['firstName'], end="\t")
            print(allRecords[i]['lastName'])
        option = 0
    elif option == 2:
        displayRecords()
        option = 0
    elif option == 3:
        inputRecords()
    else:
        print("Invalid Choice")
    time.sleep(2)
    print()
    print()
    print("Option 1 - Display Names")
    print("Option 2 - Display all information")
    print("Option 3 - Enter Data")
    print("Option 4 - Exit")

    option = int(input("Select option 1 - 4: "))

print("\nEnd Program")




