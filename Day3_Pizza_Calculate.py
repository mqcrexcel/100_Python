print("Welcome to Manh Quan Pizza's Company")
size = input("Which size you want ? S, M or L ? ")
money = 0
if size == "S" or "s":
    money = money + 15

    if input("Did you want Pepperoni ? Y or N ") == "Y":
        money = money + 2
    elif input("Did you want Pepperoni ? Y or N ") == "N":
        # Do nothing
        pass    
    else:
        # Do nothing
        pass

    if input("Did you want more cheese ? Y or N ") == "Y":
        money = money + 1
    elif input("Did you want more cheese ? Y or N ") == "Y":
        # Do nothing
        pass
    else:
        print("Wrong option extra cheese!!")

if size == "M" or size == "L" or size == "m" or size == "l":
    money = money + 15

    if input("Did you want Pepperoni ? Y or N ") == "Y" or "y":
        money = money + 2
    elif input("Did you want Pepperoni ? Y or N ") == "N" or "n":
        # Do nothing
        pass    
    else:
        # Do nothing
        pass
    
    if input("Did you want more cheese ? Y or N ") == "Y":
        money = money + 1
    elif input("Did you want more cheese ? Y or N ") == "Y":
        # Do nothing
        pass
    else:
        print("Wrong option extra cheese!!")
