#Tasks:
#The total number of votes cast -voter ID
#A complete list of candidates who received votes - candidate
#The percentage of votes each candidate won 
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#import dependencies
import os
import csv

#define variables
candidate = []
votes = []
vote_percentage = []
total_votes=0

election_data = os.path.join("election_data.csv")

with open(election_data) as csvfile: 
    csvreader = csv.reader(csvfile,delimiter=",")
    election_header = next(csvreader)
    print(election_header)

    for row in csvreader:
        #count number of votes
        total_votes += 1

        #loop through list; use "not in" operator to identify new candidate
        if row[2] not in candidate:
            candidate.append(row[2])
            #add new candidate to list
            candidatelist = candidate.index(row[2])
            #count corresponding votes
            votes.append(1)
        #otherwise, add vote to candidate
        else:
            candidatelist = candidate.index(row[2])
            votes[candidatelist] += 1

    #calculate percentage
    for elected in votes:
        percentage = (elected/total_votes)*100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        vote_percentage.append(percentage)

        #print(percentage)

    #winner
    winning_number =max(votes)
    candidatelist = votes.index(winning_number)
    winner = candidate[candidatelist]


print("Election Results")
print("--------------------------------------")
print(f"Total votes: {str(total_votes)}")
print("--------------------------------------")
for c in range(len(candidate)):
    print(f"{candidate[c]}:{str(vote_percentage[c])} ({str(votes[c])})")
print("--------------------------------------")
print(f"Winner:{winner}")
print("--------------------------------------")