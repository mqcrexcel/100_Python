# Get input from user
num_height = float(input("Please key-in your height: \n"))
num_weight = float(input("Please key-in your weight: \n"))

# Calculate processing
bmi_value = num_weight/num_height**2
# Using "format" method will return str
bmi_two_dec_format = "{:.2f}".format(bmi_value)
# Using rounf function will return float
bmi_two_dec_round  = round(bmi_value,3)

# Print result
print(type(bmi_two_dec_format))
print(type(bmi_two_dec_round))
print("Your BMI is: " + bmi_two_dec_format + " (format method)")
print("Your BMI is: " + str(bmi_two_dec_round) + " (round function)")
print(f"Your height is {num_height}, your weight is {num_weight}, your BMI is {bmi_two_dec_round}")

# Interpreataion of their BMI
if 18.5 > bmi_two_dec_round:
    print("You are underweight !")
else:
    if 25 > bmi_two_dec_round:
        print("You are normal weight")
    elif 30 > bmi_two_dec_round:     
        print("You are overweight") 
    elif 35 > bmi_two_dec_round:
        print("You are obse") 
    else:
        print("You are clinically obse")        