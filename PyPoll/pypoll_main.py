#PyBank Challenge Micah Raquena-Pequeno 16.03.23
#import dependencies
import os
#Module for reading CSV file
import csv

#reading in a file
# pypoll_path = os.path.join('Resources','election_data.csv')
# with open(pypoll_path,encoding='utf') as pypoll_csv:   
#     pypoll_reader = csv.reader(pypoll_csv,delimiter=',')
#     print(pypoll_reader)
#     pybank_header = next(pypoll_reader)
#     print(f"CSV Header: {pybank_header}")
#     for row in pypoll_reader:
#         print(row)

#-----------------------------------------

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

pypollpath = os.path.join('Resources','election_data.csv')

#Set up lists 
balot_id = [] #'Provit/Losses'
country = []
candidates = []



# Read the csv and set it up as list dictionary
with open(pypollpath,encoding='utf') as pypoll_csv: 
    pypollreader = csv.reader(pypoll_csv,delimiter=',')

    # skip first row using next
    next(pypollreader) 

    # read each row into columns/ used excel to confirm candidates. 
    for row in pypollreader:
        balot_id.append(row[0])
        country = [].append(row[1])
        candidates = [].append(row[2])
        Stockham = []
        DeGette = []
        Doane = []
    
    total_votes = len(balot_id)
     # A complete list of candidates who received votes and the total number of votes each candidate won.
    if candidates is not None:
        for row in candidates:
            if row == "Charles Casper Stockham":
                Stockham.append(candidates)
                
            elif row == "Diana DeGette":
                DeGette.append(candidates)
                
            else:
                Doane.append(candidates)
                
    votes_Stockham = len(Stockham)
    votes_Degette= len(DeGette)
    votes_Doane = len(Doane)
    p_Stockham = round(((votes_Stockham/ total_votes) * 100), 2)
    p_DeGette = round(((votes_Degette / total_votes) * 100), 2)
    p_Doane = round(((votes_Doane / total_votes) * 100), 2)

    print ("Election Results")
    print("---------------------------------------------")
    print("Total Votes: ", total_votes)                
    print(f"Stockham: %{p_Stockham} ({votes_Stockham})")
    print(f"DeGette: %{p_DeGette} ({votes_Degette})")
    print(f"Doane: %{p_Doane} ({votes_Doane})")

    # The percentage of votes each candidate won.

    # The winner of the election based on popular vote.
    def winner(candidates):
        return max(set(candidates), key = candidates.count)

    # print("Winner:", min_pl_change_date,"($", round(min_pl_change),")")
    print(candidates)
