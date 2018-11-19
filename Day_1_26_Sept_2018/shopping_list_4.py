#Shopping List
shopping_list = []

# Defining function for help
def show_help():
    print("What do you want to store in your list")
    print("Enter DONE to quit")
    print("Enter SHOW to see list")

# Defining function to see items in the list
def show_list():
    print("\"Here is your list\"")
    for x in shopping_list:
        print(x)
        
# Defining functin to add items in the list
def add_to_list(name):
    split = items.split()
    shopping_list.extend(split)

# Loop of list
while True:
    # Take Input
    items = raw_input("Enter items : ")

    # Enter DONE to quit
    if(items == "DONE"):
        break

    # To show list
    if(items == "SHOW"):
        show_list()

    # For Help    
    elif(items == "HELP"):
        show_help()

    # To add items    
    else:
        add_to_list("Add items")
