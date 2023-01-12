#import modules
import os
import csv

# import csv file 
csvpath = os.path.join('Resources', 'election_data.csv')
file = open(csvpath, newline = '')
reader = csv.reader(file)

# create output filepath 
report_to_output = os.path.join('Analysis', 'PypollReport.txt')

#create variables
voter_count = 0
stockham_votes = 0
degette_votes = 0
doane_votes = 0
stockham_percentage = 0
degette_percentage = 0
doane_percentage = 0

# read the csv file 
with open(csvpath) as voter_data:
    reader = csv.reader(voter_data)

    # establish first row as header row 
    header = next(reader) 

    #iterate through rows to count votes
    for row in reader:
        voter_count += 1

    #create if statements to tally unique values 
        if row[2] == "Charles Casper Stockham":
            stockham_votes += 1
        elif row[2] == "Diana DeGette":
            degette_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            doane_votes += 1

    #create dictionary of results 
        results = {
        "Charles Casper Stockham": (stockham_votes),
        "Diana DeGette": (degette_votes),
        "Raymon Anthony Doane": (doane_votes)
        }

        # results = [(stockham_votes), (degette_votes), (doane_votes)]

        #calculate percentage of votes for each candidate
        stockham_percentage = (stockham_votes)/(voter_count) * 100
        degette_percentage = (degette_votes)/(voter_count) * 100
        doane_percentage = (doane_votes)/(voter_count) * 100

        winner = max(results, key=results.get)


#create final report
report = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {voter_count} \n"
    f"----------------------------\n"
    f"Charles Casper Stockham: {stockham_percentage}%, ({stockham_votes})\n"
    f"Diana DeGette: {degette_percentage}% ({degette_votes})\n"
    f"Raymon Anthony Doane: {doane_percentage}% ({doane_votes})\n"
    f"----------------------------\n"
    f"Winner: {winner}"
)

#print report to terminal
print(report)

#output results to analysis folder
with open(report_to_output, 'w') as text_file:
    text_file.write(report) 