print("Welcome to Manh Quan Pizza's Company")

# Get input of Pizza size
size = input("Which size you want ? S, M or L ? ")
money = 0
print(size)

# If Pizza size is S
if size == "S" or size == "s":
    money = money + 15
    print("+15$ for size S")
    
    # Get input option for pepperoni
    option_pep = input("Did you want pepperoni ? Y or N ")
    if option_pep == "Y" or "y":
        money = money + 2
        print("+2$ for pepperoni")
    elif option_pep == "N" or "n":
        print("+0$ for pepperoni")  
    else:
        print("Wrong option pepperoni!!")

    # Get input option for extra cheese
    option_che = input("Did you want more cheese ? Y or N ")
    if option_che == "Y" or "y":
        money = money + 1
        print("+1$ for cheese")
    elif option_che == "N" or "n":
        print("+0$ for cheese")
    else:
        print("Wrong option extra cheese!!")

# If Pizza size is M or L
elif size == "M" or size == "L" or size == "m" or size == "l":
    money = money + 18
    print("+18$ for size L or M")
    
    option_pep = input("Did you want pepperoni ? Y or N ")
    if option_pep == "Y" or "y":
        print("+3$ for pepperoni")
        money = money + 3
    elif option_pep == "N" or "n":
        print("+0$ for pepperoni")   
    else:
        print("Wrong option pepperoni!!")
    
    option_che = input("Did you want more cheese ? Y or N ")
    if option_che == "Y" or "y":
        money = money + 1
        print("+1$ for cheese")
    elif option_che == "N" or "n":
        print("+0$ for cheese")
    else:
        print("Wrong option extra cheese!!")

# If input not correct
else: 
    print("Wrong size of Pizza")

# Print out result
print("You need to pay: " + str(money))