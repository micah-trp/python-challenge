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

# Read the csv and set it up as list dictionary
with open(pypollpath,encoding='utf') as pypoll_csv: 
    pypollreader = csv.reader(pypoll_csv,delimiter=',')

    # skip first row using next
    next(pypollreader) 

    #Set up lists 
    balot_id = [] #'Provit/Losses'
    country = []
    candidtates = []

    # read each row into columns
    for row in pypollreader:
        balot_id.append(row[0])
        country = [].append(row[1])
        candidtates = [].append(row[2])

    print ("Election Results")
    print("---------------------------------------------")
    print("Total Votes: ", len(balot_id))

    # for i in range(1,len(prof_loss)):

    #     pl_change.append(prof_loss[i] - prof_loss[i-1])   
        
    #     avg_pl_change = sum(pl_change)/len(pl_change)

    #     max_pl_change = max(pl_change)
    #     max_pl_change_date = str(date[pl_change.index(max(pl_change))])

    #     min_pl_change = min(pl_change)
    #     min_pl_change_date = str(date[pl_change.index(min(pl_change))])


    # print("Avereage Change: $", round(avg_pl_change))
    # print("Greatest Increase in Profits:", max_pl_change_date,"($", round(max_pl_change),")")
    # # print("Greatest Decrease in Profits:", min_pl_change_date,"($", round(min_pl_change),")")
    
    # print("Winner:", min_pl_change_date,"($", round(min_pl_change),")")
    print(candidtates)
