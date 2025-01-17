import os
import csv

csvpath = "./Resources/election_data.csv"
out_file = "./Analysis/output.txt"

TotalVotes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    voterID = csv_header.index('Voter ID')
    candidate = csv_header.index('Candidate')
    county = csv_header.index('County')
    candList = []
# Read Each row
    for row in csvreader:
        # The total number of votes cast
        TotalVotes = TotalVotes + 1

# A complete list of candidates who received votes
        candList.append(str(row[candidate]))
    unique_candList = list(set(candList))

# The total number of votes each candidate won
    votes1 = unique_candList[0]
    votes1_count = candList.count(votes1)
    votes2 = unique_candList[1]
    votes2_count = candList.count(votes2)
    votes3 = unique_candList[2]
    votes3_count = candList.count(votes3)
    votes4 = unique_candList[3]
    votes4_count = candList.count(votes4)
# The percentage of votes each candidate won
    votes1_p = round((votes1_count / TotalVotes) * 100)
    votes2_p = round((votes2_count / TotalVotes) * 100)
    votes3_p = round((votes3_count / TotalVotes) * 100)
    votes4_p = round((votes4_count / TotalVotes) * 100)

# The winner of the election based on popular vote.
    maxList = [votes1_p, votes2_p, votes3_p, votes4_p]
    win = max(maxList)
    if win == votes1_p:
        winner = votes1
    elif win == votes2_p:
        winner = votes2
    elif win == votes3_p:
        winner = votes3
    elif win == votes4_p:
        winner = votes4
# RESULTS
print("--------------------------")
print(f"Total Votes: {TotalVotes}")
print("--------------------------")
print(f"{votes1}: {votes1_p}.00%({votes1_count})")
print(f"{votes2}: {votes2_p}.00%({votes2_count})")
print(f"{votes3}: {votes3_p}.00%({votes3_count})")
print(f"{votes4}: {votes4_p}.00%({votes4_count})")
print("--------------------------")
print(f"Winner: {winner}")

# Write outfile
with open(out_file, 'w') as outputFile:
    outputFile.write("-------------------------")
    outputFile.write("Total Votes: {TotalVotes}")
    outputFile.write("-------------------------")
    outputFile.write(f"{votes1}: {votes1_p}.00%({votes1_count})")
    outputFile.write(f"{votes2}: {votes2_p}.00%({votes2_count})")
    outputFile.write(f"{votes3}: {votes3_p}.00%({votes3_count})")
    outputFile.write(f"{votes4}: {votes4_p}.00%({votes4_count})")
# -------------------------
# Total Votes: 3521001
# -------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
#Winner: Khan
# -------------------------
