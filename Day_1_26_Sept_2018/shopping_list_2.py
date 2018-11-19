#Shopping List
shopping_list = []
print("What do you want to store in your list")
print("Enter DONE to quit")
print("Enter SHOW to see list")

# Loop of list
while True:
    # Take Input
    items = raw_input("Enter items : ")

    # Enter DONE to quit
    if(items == "DONE"):
        break
    # To show list
    if(items == "SHOW"):
        print("\"Here is your list\"")
        for x in shopping_list:
            print(x)
    # For Help    
    elif(items == "HELP"):
        print("Enter DONE to quit")
        print("Enter SHOW to see list")

    # To add items    
    else:
        shopping_list.append(items)
