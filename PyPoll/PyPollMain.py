import csv
import os
import itertools

#path
csvpath = os.path.join("Resources", "election_data.csv")

#variables 
candidates = []
total_votes = 0

#open file
with open(csvpath, newline='') as votes:
  csvreader = csv.DictReader(votes)


  for row in itertools.islice(csvreader, 1, None):
    
    #Tally 
    if row["Candidate"] not in candidates:
      total_votes += 1
      candidates.append(row["Candidate"])
    else: 
      total_votes += 1
      
      
i = 0

#vote_count with a number of values=candidates list
length = len(candidates)
vote_count = [0] * length 

#file reload
with open(csvpath, newline='') as votes:
  csvreader = csv.reader(votes)
  for row in itertools.islice(csvreader, 1, None): 
    
    #tally 1 vote for each candidate name here
    for i in range(length):
      if row[2] == candidates[i]:
        vote_count[i] += 1

        #each candidate variable
j = 0       
percent_votes = []
      
      # percent of total votes being add to the percent_votes list
for j in range(length):
  pv = round(vote_count[j] / total_votes * 100.00, 2)
  percent_votes.append(pv)

    #max_votes
    max_votes = max(vote_count)
    #index of the max_votes value
    max_index = vote_count.index(max_votes)
    #election winner 
    election_winner = candidates[max_index]

#printing output
print("ELECTION RESULTS")
print("---------------------------------------------------")
for (x, y, z) in zip(candidates, percent_votes, vote_count):
    print("Name: ", x ,"; Percent: ", y, "; Total Votes: ", z )
print("---------------------------------------------------")
print("Total votes: " + str(total_votes))
print("---------------------------------------------------")
print("Winner: " + str(election_winner))
#New File
filename = "results.txt"

#output file
line1= results = open("results.txt","w")
results.write("ELECTION RESULTS")
results.write("\n-----------------------------------")
for (x, y, z) in zip(candidates, percent_votes, vote_count):
    results.write("\n\nName: {}, {}, {}".format(x,y,z))
results.write('\n\n-------------------------------------')
results.write("\n\nTotal votes: " + str(total_votes))
results.write('\n\n--------------------------------------')
results.write("\n\nWinner: " + str(election_winner))
results.close()



