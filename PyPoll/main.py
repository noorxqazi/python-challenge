#import modules to read and file 

import os
csvpath = os.path.join('Resources', 'election_data.csv')

import csv
with open (csvpath, newline= '') as csvfile:

#specify delimiter 
    csvreader = csv.reader(csvfile, delimiter = ',') 

#read each row 
with open (csvpath, 'r') as csvfile:
 for row in csvfile:

# count the number of rows to calculate number of votes 
     row_count = len(csvpath)

# subtract 1 to exclude the header row
row_count -= 1

print(f"Number of votes: {row_count}")