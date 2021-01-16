def insert(contacts) :
    while(1):
        a = input("Enter name (type exit to exit the insert mode) :")
        if a == 'exit' :
            break
        b = input("Enter contact number :")
        contacts[a] = b
    contacts = sorted(contacts.items())
    contacts = {x:y for x,y in contacts}
    return contacts

def key_search(contacts) :
    count = 0
    names = {}
    while(1) :
        key = input("Enter the keyword to be searched (type exit to exit this mode) :")
        if key == 'exit' :
            break
        for name in contacts.keys() :
            if key in name :
                names[count] = name
                count += 1
        if count == 0 :
            print("Error!!!!  This keyword does not exist")
        if count == 1 :
            print("Name : " + str(names[0])) 
            print("Contact Number : " + str(contacts[names[0]]))
        if count > 1 :
            for i in range(count) :
                print(str(i) + " : " + str(names[i]))
            name = input("Choose the desired name(type the index before the name) : ") 
            print("Contact Number : " + str(contacts[names[int(name)]]))

def switch(contacts) :
    while(1) :
        arg = input("Enter a query : ")
        if arg == '1' :
            contacts = insert(contacts)
        elif arg == '2' :
            key_search(contacts)
        elif arg == '3' :
            print(contacts)
        else : 
            break
    return contacts

contacts = {}
print("Query List :")
print("1 : Insert a new contact")
print("2 : Retrieve details about a contact")
print("3 : Print the contact list (shows that contacts are always stored in dictionary order)")
print("Enter anything else to exit")
contacts = switch(contacts)