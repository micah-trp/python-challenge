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
#  
pybankpath = os.path.join('Resources','budget_data.csv')

# Read the csv and set it up as list dictionary
with open(pybankpath,encoding='utf') as pybank_csv: 
    pybankreader = csv.reader(pybank_csv,delimiter=',')

    # skip first row using next
    next(pybankreader) 

    #Set up lists 
    prof_loss = [] #'Provit/Losses'
    date = []
    pl_change = []

    # in this loop count total months from date - column [0] and did sum of prof_loss (Profit/Losses)- column [1] 
    for row in pybankreader:
        date.append(row[0])
        prof_loss.append(float(row[1]))   

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total: $", sum(prof_loss))

    #in this loop I did total of difference between all row of column "prof_loss" and found total revnue change. Also found out max prof_loss change and min prof_loss change. 
    for i in range(1,len(prof_loss)):

        pl_change.append(prof_loss[i] - prof_loss[i-1])   
        
        avg_pl_change = sum(pl_change)/len(pl_change)

        max_pl_change = max(pl_change)
        max_pl_change_date = str(date[pl_change.index(max(pl_change))])

        min_pl_change = min(pl_change)
        min_pl_change_date = str(date[pl_change.index(min(pl_change))])


    print("Avereage Change: $", round((avg_pl_change),2))
    print("Greatest Increase in Profits:", max_pl_change_date,"($", round(max_pl_change),")")
    print("Greatest Decrease in Profits:", min_pl_change_date,"($", round(min_pl_change),")")


# Validation ---------------------------------------------

# Validation: total months = 86
# counter = defaultdict(int)
# with open(pybankpath,encoding='utf') as pybank_csv: 
#     reader = csv.DictReader(pybank_csv)
#     for row in reader:
#         counter[row['Date']] += 1
# print('Total Months :',(len(dict(counter))))


# Validation Total $22564198.0
# with open(pybankpath,encoding='utf') as pybank_csv: 
#     headerline = next(pybank_csv)
#     total = 0
#     for row in csv.reader(pybank_csv):
#         total += int(row[1])
#     print('Total : $' , total)


#--------------------------------------------


#Write to text file

output_path = os.path.join('Resources',"pybank_result.txt")

file =  open(output_path, 'w') 

file.write(f"Financial Analysis\n")
file.write(f"-----------------------------------\n")
file.write(f"Total Months: {len(date)}\n")
file.write(f"Total: $ {sum(prof_loss)}\n")
file.write(f"Avereage Change: $ {round((avg_pl_change),2)}\n")
file.write(f"Greatest Increase in Profits:{ max_pl_change_date}, ${round(max_pl_change)}\n")
file.write(f"Greatest Decrease in Profits:{ min_pl_change_date}, ${round(min_pl_change)}\n")
file.write("----------------------------\n")

file.close()
