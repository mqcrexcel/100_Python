# Get input data
str_two_Number = input("Please keyin 2 number: ")

# Try to covert data type from str to int. If can, then print out result, if not then print out warning  
try:
    first_num = int(str_two_Number[0])
    second_num = int(str_two_Number[1])
    total_num =  first_num + second_num
    print("Total of " + str_two_Number[0] + " and " + str_two_Number[1] + " is " + str(total_num))    

except:
    print("Please check your input, look like it not interger")    