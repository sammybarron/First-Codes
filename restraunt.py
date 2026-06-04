# Ask the user for the total bill amount
total_bill = float(input("How much was your bill today? "))
# Ask the user what percentage they want to tip
tip_percentage = float(input("What percentage would you like to tip today? ")) 
# Calculate the total tip amount
tip_amount = total_bill * (tip_percentage / 100)
# Print the result 
print(tip_amount + total_bill)