num_height = float(input("Please key-in your height: \n"))
num_weight = float(input("Please key-in your weight: \n"))

bmi_value = num_weight/num_height**2
bmi_two_decimal = "{:.2f}".format(bmi_value)

print("Your BMI is: " + bmi_two_decimal)