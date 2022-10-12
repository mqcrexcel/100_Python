age = input("What your current age? \n")

days_left = (90 - int(age)) * 365
weeks_left = (90 - int(age)) * 52
month_left = (90 - int(age)) * 12

print(f"You have {days_left} days, {weeks_left} weeks, {month_left} months if you live until 90 year old")