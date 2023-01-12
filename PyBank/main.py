# import modules and read csv files
import os
import csv
import statistics

csvpath = os.path.join('Resources', 'budget_data.csv')
file = open(csvpath, newline = '')
reader = csv.reader(file)

# create output filepath 
report_to_output = os.path.join('Analysis', 'BudgetReport.txt')


# create variables
total_months = 0
net_total = 0

monthly_changes = []
changes = []
avg_changes = 0

greatest_increase = 0
greatest_month = ''
greatest_decrease = 0
worst_month = ''


# read the csv file 
with open(csvpath) as bank_data:
    reader = csv.reader(bank_data)

    # establish first row as header row 
    header = next(reader) 

    # extract first row
    first_row = next(reader)

    # increment total months by one
    total_months += 1

    # increment net total
    net_total = int(first_row[1])

    # increment changes 
    # monthly_changes = int(first_row[1])

    #increment avg changes
    avg_changes = int(first_row[1])

    # iterate through rest of csv file
    for row in reader:

        #capture total months 
        total_months += 1

        #capture total net profit losses
        net_total += int(row[1])

      
        # # calculate avg changes 
        # monthly_changes = int(row[1])- previous_profit
        # previous_profit = int(row[1]) - 1
        # monthly_changes_list = monthly_changes_list + [monthly_changes]
        # month_of_profit = [month_of_profit] + [row[0]]
        # avg_changes = sum(monthly_changes_list) / len(monthly_changes_list)

        # #calculate monthly changes
        # for i in range(len(net_total)-1):
        #      monthly_changes_list.append(net_total[i+1]-net_total[i])
        #      avg_changes = (sum(monthly_changes_list)/len(monthly_changes_list))"
        
        #create if statements to calculate greatest/worst months of profit 
        if int(row[1]) > greatest_increase:
            greatest_month = (row[0])
            greatest_increase = int(row[1])

        elif int(row[1]) < greatest_decrease:
            worst_month = (row[0])
            greatest_decrease = int(row[1])
        changes.append(int(row[1]))

        #calculate monthly changes 
        for i in range(len(changes)-1):
            total_changes = (changes[i+1]- changes[i])
            monthly_changes.append(total_changes)

            avg_changes = statistics.mean(monthly_changes)





# create report
report = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Avg Change:" + str(round(avg_changes, 2))
)

# print to terminal
print(report)


# output results to analysis folder
with open(report_to_output, 'w') as text_file:
    text_file.write(report)