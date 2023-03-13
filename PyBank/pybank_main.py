#PyBank Challenge Micah Raquena-Pequeno D
#import dependencies
import os
#Module for reading CSV file
import csv
pybankpath = os.path.join('/','Resources','budget_data.csv')

# Read in the CSV file
with open(pybankpath,encoding='utf') as pybank_csv:   
    # Split the data on commas
    pybankreader = csv.reader(pybank_csv,delimiter=',')
    pybank_header = next(pybankreader)

    #print(pybankreader)
    print(f"CSV Header: {pybank_header}")

    for row in pybankreader:
        print(row)


#create output title
print("Financial Analysis")
print("---------------------------------------------")

#Average Change
print("Average Change:")

#Greatest Increase In Profits
print("Greatest Increase in PRofits:")

#Greatest Decrease IN Profits
print("Greatest Decrease in Profits:")

#Count total months
total_months = len(list(pybankreader))
print("Total Months:"+total_months)

#create total 
total = sum("Profit/Losses")
print("total:"+total)

