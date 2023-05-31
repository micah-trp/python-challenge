#PyBank Challenge Micah Raquena-Pequeno 
#import dependencies
import os
#Module for reading CSV file
import csv

# from collections import defaultdict
#-------------------------------------------------------------------------
# Read in the CSV file
# with open(pybankpath,encoding='utf') as pybank_csv:   
#     # Split the data on commas
#     pybankreader = csv.reader(pybank_csv,delimiter=',')
#     pybank_header = next(pybankreader)

#     #print(pybankreader)
#     print(f"CSV Header: {pybank_header}")

#     for row in pybankreader:
#         print(row)
#-------------------------------------------------------------------------

 
pybankpath = os.path.join('Resources','budget_data.csv')

# Read the csv and set it up as dictionairies
with open(pybankpath,encoding='utf') as pybank_csv: 
    pybankreader = csv.reader(pybank_csv,delimiter=',')

    # skip first row using next
    next(pybankreader) 
    revenue = [] #'Provit/Losses'
    date = []
    rev_change = []

    # in this loop count total months fromo Date [0] and did sum of revenue (Profit/Losses) [1] 
    for row in pybankreader:
        date.append(row[0])
        revenue.append(float(row[1]))   

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))

    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    print("Avereage Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", round(max_rev_change),")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", round(min_rev_change),")")


# Validation ---------------------------------------------

# Validation: total months
# counter = defaultdict(int)
# with open(pybankpath,encoding='utf') as pybank_csv: 
#     reader = csv.DictReader(pybank_csv)
#     for row in reader:
#         counter[row['Date']] += 1
# print('Total Months :',(len(dict(counter))))


# Validation Total
# with open(pybankpath,encoding='utf') as pybank_csv: 
#     headerline = next(pybank_csv)
#     total = 0
#     for row in csv.reader(pybank_csv):
#         total += int(row[1])
#     print('Total : $' , total)


#--------------------------------------------