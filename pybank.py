#pybank homework
import os
import csv

# Path to collect bank data from the Pythonstuff folder
pybankbudgetdata_csv = os.path.join('..', 'Election_Homework', 'pybankbudgetdata.csv')

Change = 0
previous = 0
total = 0
total_dollars = 0
Greatest_increase = 0
sum = 0
sum_total = 0
Greatest_Decrease = 9999999999999999999

#open csv
with open(pybankbudgetdata_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        total = total + 1
        if total > 1:
            Change = int(row[1]) - previous
            sum = sum + Change

            if Change > Greatest_increase:
                Greatest_increase = Change

            if Change < Greatest_Decrease:
                Greatest_Decrease = Change

        previous = int(row[1])
        sum_total = sum_total + int(row[1])

print( "Average Change $ " + str(sum / (total - 1)))
print("Total Months " + str(total))
print("Total Dollars $ " + str(sum_total))
print("Greatest Increase in Profits: $ " + str(Greatest_increase))
print("Greatest Decrease in Profits: $ " + str(Greatest_Decrease))




