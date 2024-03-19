print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip_percentage = tip / 100

number_split = int(input("How many people split the bill? "))

total_each = (total_bill + (total_bill * tip_percentage)) / number_split

total_each_rounded = round(total_each, 2)

final_amount = "{:.2f}".format(total_each)

print(f"Each person should pay: ${final_amount} each")