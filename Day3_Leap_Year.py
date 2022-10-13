num_year = int(input("What year you want to check? "))

if num_year % 4 == 0:
    if num_year % 100 == 0:
        if num_year % 400 == 0:
            print("This year is Leap Year") 
        else:
            if (num_year / 100) % 4 == 0:
                print("This year is Leap Year")
            else:
                print("This year isn't Leap Year")  
    else:
        print("This year is Leap Year")
else:        
    print("This year isn't Leap Year")                       