print("Welcome to the tip calculator!")

# Get the bill amount
total : float = float(input("What was the total bill? $"))

# Get the percent of tip
tip : float  = int(input("How much tip would you like to give? 10, 12, or 15? "))/100

# Get the number of people
people : int = int(input("How many people to split the bill? "))

# Calculate bill by adding the total plus the tip amount, then divide it by the number of people. Cap it off by rounding to 2 decimal places
bill = round((total + (total * tip)) / people,2) 
print(f"Each person should pay: {bill}")
