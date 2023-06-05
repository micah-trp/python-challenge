#PyBank Challenge Micah Raquena-Pequeno 16.03.23
#import dependencies
import os 
#Allow us to read csv file
import csv

#list total_votes
total_total_votes = []

#dictionary for each row
canidate_total_votes = {}

#Candidates - using names from csv list.
Stockham = 0
Doane = 0
DeGette = 0

pypoll_path = os.path.join('Resources','election_data.csv')

#--------------------main loop-----------------
#read csv file
with open(pypoll_path) as pypoll_csv:
    csvreader = csv.reader(pypoll_csv, delimiter=',')
    #----------skip header row
    next(csvreader)
    

    #-------read for total_votes
    for csvrow in csvreader:
            total_votes.append(csvrow[1])
            total_votes = len(total_votes)

    #-------validate total votes row
    # print(total_votes)  

        #Add to count, if value candidate is located in column [2]
        # use conditon to assign to each candidate
            if csvrow[2] == "Charles Casper Stockham":
                Stockham += 1
    #print(Stockham)

            elif csvrow[2] == "Diana DeGette":
                DeGette +=1
    #print(DeGette)

            elif csvrow[2] == "Raymon Anthony Doane":
                Doane +=1
    #print(Doane)

    #Canidate Calculation
    Canidate_stockham = round((Stockham/total_votes)*100,3)
    Canidate_degette = round((DeGette/total_votes)*100,3)
    Canidate_doane = round((Doane/total_votes)*100,3)

    #total_votes by candidate dictionary
    Canidate_total_votes = {"Charles Casper Stockham": Stockham, "Diana DeGette": DeGette, "Raymon Anthony Doane": Doane }  

    winner = max(Canidate_total_votes, key=Canidate_total_votes.get)
    #print(winner)   


#Write to text file
output_path = "election_result.txt"

file =  open(output_path, 'w') 


file.write("Election Results\n")
file.write("----------------------------\n")
file.write(f"Total total_votes: {total_votes}\n")
file.write("----------------------------\n")
file.write(f"Charles Casper Stockham: {Canidate_stockham}% ({Stockham})\n")
file.write(f"Diana DeGette: {Canidate_degette}% ({DeGette})\n")
file.write(f"Raymon Anthony Doane: {Canidate_doane}% ({Doane}) \n")
file.write("----------------------------\n")
file.write(f"Winner: {winner}\n")

file.close()
