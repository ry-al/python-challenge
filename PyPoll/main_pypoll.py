# Python Homework

import os
import csv

csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

voter_id = []
county = []
candidate_list = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate_list.append(row[2])


#The total number of votes cast

voter_id_count = len(voter_id)


# A complete list of candidates who received votes

candidate_set = set(candidate_list)


# The total number of votes each candidate won

khan_count = 0
correy_count = 0
li_count = 0
otooley_count = 0

for row in candidate_list:
    if row == "Khan":
        khan_count += 1
    elif row == "Correy":
        correy_count += 1
    elif row == "Li":
        li_count += 1
    elif row == "O'Tooley":
        otooley_count += 1

poll_count = {"Khan": khan_count, "Correy": correy_count, "Li": li_count, "O'Tooley": otooley_count}


# The percentage of votes each candidate won

total_votes = khan_count + correy_count + li_count + otooley_count
khan_percent = format((khan_count/ total_votes), "%")
correy_percent = format((correy_count / total_votes), "%")
li_percent = format((li_count / total_votes), "%")
otooley_percent = format((otooley_count / total_votes), "%")


# # The winner of the election based on popular votes

total_votes_list = [khan_count, correy_count, li_count, otooley_count]
winner_count = max(total_votes_list)

winner_index = 0
for count in total_votes_list:
    if count == winner_count:
        winner_index = 0       

if winner_index == 0:
    winner = "Khan"
elif winner_index == 1:
    winner = "Correy"
elif winner_index == 2:
    winner = "Li"
elif winner_index == 3:
    winner = "O'Tooley"

#Output

print("Election Results")
print("-------------------------------")
print(f"Total Votes: {voter_id_count}")
print("-------------------------------")
print(f"Khan: {khan_percent} ({(khan_count)})")
print(f"Correy: {correy_percent} ({correy_count})")
print(f"Li: {li_percent} ({li_count})")
print(f"O'Tooley: {otooley_percent} ({otooley_count})")
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")



# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------