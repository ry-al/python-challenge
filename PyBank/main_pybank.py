# Python Homework

import os
import csv

csvpath = os.path.join('..', 'PyBank', 'budget_data.csv')

print(csvpath)

months = []
PL = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        months.append(row[0])
        PL.append(row[1])


# The total number of months included in the dataset
months_count = len(months)

# The net total amount of "Profit/Losses" over the entire period
PL_sum = 0
for row in PL:
    PL_sum = PL_sum + int(row)


# The average of the changes in "Profit/Losses" over the entire period
# Formula: Sum of (previous PL - new PL)/ total number

change_profit = []
for row in PL:
    change_profit_difference =  PL[row]
    change_profit.append(change_profit_difference)

print(change_profit_difference)

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire perio

# Output
# print("Financial Analysis")
# print("---------------------------------------")
# print(f"Total Months: {months_count}")
# print(f"Total: ${PL_sum}")
# print(f"Average Change: {PL_sum.average()}")
