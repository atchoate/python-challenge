import os
import csv

csv_path = os.path.join("Resources", "election_data.txt")

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    votes = []

    for row in csvreader:
        votes.append(row[0])
    
    total_votes = len(votes)
    print("ELECTION RESULTS")
    print("-----------------------------------------")
    print("Total votes: " + str(total_votes))

print("---------------------------------------------")

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    candidates = []
    
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
    print("Candidates: " + str(candidates))

print("---------------------------------------------")

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    for row in csvreader:
        if row[2] == 'Khan':
            khan_votes = khan_votes + 1
        if row[2] == 'Correy':
            correy_votes = correy_votes + 1
        if row[2] == 'Li':
            li_votes = li_votes + 1
        if row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1

    khan_percent = (khan_votes / total_votes) * 100    
    correy_percent = (correy_votes / total_votes) * 100  
    li_percent = (li_votes / total_votes) * 100  
    otooley_percent = (otooley_votes / total_votes) * 100   

    print("Khan: " + str(khan_votes) + " votes, " + str(khan_percent) + " percent")
    print("Correy: " + str(correy_votes) + " votes, " + str(correy_percent) + " percent")
    print("Li: " + str(li_votes) + " votes, " + str(li_percent) + " percent")
    print("O'Tooley: " + str(otooley_votes) + " votes, " + str(otooley_percent) + " percent")

print("----------------------------------------------------")

final_dict = {
    "Khan ":khan_votes,
    "Correy ":correy_votes,
    "Li ": li_votes,
    "O'Tooley":otooley_votes
}

winner = max(final_dict.keys(), key=(lambda k: final_dict[k]))
print("Winner: " + winner)


print("ELECTION RESULTS", file=open("election_results.txt", "a"))
print("-----------------------------------------", file=open("election_results.txt", "a"))
print("Total votes: " + str(total_votes), file=open("election_results.txt", "a"))

print("---------------------------------------------", file=open("election_results.txt", "a"))

print("Khan: " + str(khan_votes) + " votes, " + str("{:.2f}".format(khan_percent)) + " percent", file=open("election_results.txt", "a"))
print("Correy: " + str(correy_votes) + " votes, " + str("{:.2f}".format(correy_percent)) + " percent", file=open("election_results.txt", "a"))
print("Li: " + str(li_votes) + " votes, " + str("{:.2f}".format(li_percent)) + " percent", file=open("election_results.txt", "a"))
print("O'Tooley: " + str(otooley_votes) + " votes, " + str("{:.2f}".format(otooley_percent)) + " percent", file=open("election_results.txt", "a"))

print("----------------------------------------------------", file=open("election_results.txt", "a"))
print("Winner: " + winner, file=open("election_results.txt", "a"))