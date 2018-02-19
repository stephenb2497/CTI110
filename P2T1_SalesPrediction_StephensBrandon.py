# CTI-110 
# P2T1 - Sales Prediction 
# Brandon Stephens
# 2/18/2018

# Ask user to input amount of total sales
total_sales = float(input("Please enter the amount of total sales:"))

# Calculate the profit margin as 23 percent of total sales.
profit = total_sales * 0.23 

# display the profit margin.
print("Your profit from sales is $", format(profit, ',.2f'))

