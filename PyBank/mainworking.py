#import modules and read csv files
import os
import csv
from datetime import datetime
csvpath = os.path.join('Resources', 'budget_data.csv')
file = open(csvpath, newline = '')
reader = csv.reader(file)

#establish first row as header row 
header = next(reader) 

#establish what data type each column of each row is 
data = []
for row in reader:

    #establish how dates are written in first column
    date_string = "JAN-10"
    format_string = "%b-%y"
    date = datetime.strptime(date_string, format_string)
    
    #establish datatype for 2nd column
    profitlosses = int(row[1])

# Assume the dataset includes dates from January 1, 2010 to December 31, 2020
start_date = datetime(2009, 12, 31)
end_date = datetime(2017, 2, 28)

# Calculate the difference in months between the start and end dates
difference = end_date.month - start_date.month
years_difference = end_date.year - start_date.year
total_months = difference + (years_difference * 12)

print("Analysis")
print("----------------------------------------")
print(f"Total number of months: {total_months}")

#calculate sum of profit/losses

for row in reader:
    total = sum(profitlosses)
  
print(total)


#calculate changes in "Profit/Losses" over the entire period, and then the average of those changes

#changes = []

#for i in range(1, len(data)):
 #   change = data[i][1] - data[i-1][1]
  #  changes.append(change)

#average_change = sum(changes) / len(changes)

#print(changes) 
#print(average_change)  


