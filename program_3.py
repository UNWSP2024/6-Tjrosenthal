# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

#Tanner Rosenthal
#2/21/2025
#Sales and Taxes

def calculate_tax():
    money_collected = float(input("How much money did you collect?"))
    state_tax = round(0.05 * money_collected, 2)
    county_tax = round(0.025 * money_collected, 2)
    return state_tax, county_tax


state, county = calculate_tax()
total = state + county
print(f"The state tax amount was ${state:.2f}")
print(f"The county tax amount was ${county:.2f}")
print(f"The total amount paid in taxes is ${total:.2f}")
