# Python Homework

import os
import csv
import statistics

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


# Compute for the average, greatest increase and decrease in profits

x = 0
max_value = 0
min_value = 0
ind = 0
max_value_index = 0
min_value_index = 0

change_profit = []
for row in PL:
    row = int(row)
    diff = row - x
    if max_value < diff:
        max_value = diff
        max_value_index = ind
    if min_value > diff:
        min_value = diff
        min_value_index = ind
    ind += 1
    x = row
    change_profit.append(diff)
    
change_profit = change_profit[1:]
PL_Average = statistics.mean(change_profit)

max_date = months[max_value_index]
min_date = months[min_value_index]

# Output
print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months: {months_count}")
print(f"Total: ${PL_sum}")
print(f"Average Change: ${PL_Average}")
print(f"Greatest Increase in Profits: {max_date} (${max_value})")
print(f"Greatest Decrease in Profits: {min_date} (${min_value})")
