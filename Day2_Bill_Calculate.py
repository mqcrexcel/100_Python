# Get input from user
print("Welcome to tip calculator.")
total_bill = input("What was the total bill? VND ")
percent_tip = input("What percentage you want to tip? 10, 12 or 15? ")
num_people = input("How many people tp split the bill? ")

# Calculate processing
# Round should pay to 2 decimal 
should_pay = round((int(total_bill) + (int(total_bill) * int(percent_tip)) / 100) / int(num_people), 2)

# Print result
print(f"Each person should pay: VND {should_pay}")