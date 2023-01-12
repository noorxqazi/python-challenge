#import modules and read csv files
import os
csvpath = os.path.join('Resources', 'budget_data.csv')

import csv
with open (csvpath, newline= '') as csvfile:

#specify delimiter 
    csvreader = csv.reader(csvfile, delimiter = ',') 
    print(csvreader)

#read each row 
    for row in csvreader:
        print(row)


#import module for datetime to calculate months 

from datetime import datetime

# Assume the dataset includes dates from January 1, 2010 to December 31, 2020
start_date = datetime(2009, 12, 31)
end_date = datetime(2017, 2, 28)

# Calculate the difference in months between the start and end dates
difference = end_date.month - start_date.month
years_difference = end_date.year - start_date.year
total_months = difference + (years_difference * 12)

print(f"Total number of months: {total_months}")


#calculate the net total amount of "Profit/Losses" over the entire period

#for row in csvreader: 
#    total_profit = 0
 #   total_profit += sum(int(cell) for cell in row)

#print(f"Total Profit: {total_profit}")

#def print_profitlosses(profit_data):
   # dates = str(profit_data[0])
    #values = int(profit_data[1])

    #total_dates = 
#
#-----------------------------------------------
  # Initialize a variable to store the total
total = 0
  
  # Iterate over the rows of the file
with open (csvpath, newline= '') as csvfile:
    for row in csvfile:

        date = str
        profit = int

    # Get the value from the second cell in the row (assuming the first cell is the month/year)
       row = [date, profit]
        row.split(date,profit)
    
        total = total + profit

print(f"Total: {total}")
#-----------------------------------------------