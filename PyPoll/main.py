# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


vote_total = 0
winner_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}

import csv
file_path = "PyPoll/Resources/election_data.csv"


    if row[2] == "Khan": 
            khan_votes +=1
    elif row[2] == "Correy":
            correy_votes +=1
    elif row[2] == "Li": 
            li_votes +=1
    elif row[2] == "O'Tooley":
            otooley_votes +=1

candidate_options = ["Kahn", "Correy", "Li", "O'Tooley"]
votes = [kkhan_votes, correy_votes,li_votes,otooley_votes ]

dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100


# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {vote_total}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({khan_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")














#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------
