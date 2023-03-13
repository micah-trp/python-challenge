#PyBank Challenge Micah Raquena-Pequeno 16.03.23
#import dependencies
import os

#Module for reading CSV file
import csv

#reading in a file
pypoll_path = os.path.join('/','Resources','election_data.csv')

with open(pypoll_path,encoding='utf') as pypoll_csv:   
    pypoll_reader = csv.reader(pypoll_csv,delimiter=',')
    
    print(pypoll_reader)

    pybank_header = next(pypoll_reader)
    print(f"CSV Header: {pybank_header}")

    for row in pypoll_reader:
        print(row)

print ("Election Results")
print("---------------------------------------------")

#The total number of votes cast

print("---------------------------------------------")

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

print("---------------------------------------------")


#The winner of the election based on popular vote
print("---------------------------------------------")
