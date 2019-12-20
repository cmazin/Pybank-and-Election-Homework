#election Homework
import os
import csv

totalvotes = 0
winner = 0
winnername = ""

electiondata_csv = os.path.join('..', 'Election_Homework', 'electiondata.csv')
candidates = {}
with open(electiondata_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        totalvotes = totalvotes + 1
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] = candidates[candidate] + 1
        else:
            candidates[candidate] = 1
for candidate, num in candidates.items():
    if num > winner:
        winner = num 
        winnername = candidate
    print(candidate + ":" + str(num) + " Percent of vote " + str(num/(totalvotes - 1) * 100))
print("Total Votes : " + str(totalvotes - 1))
print("Winner : " + winnername)

