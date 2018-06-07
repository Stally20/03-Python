#Bring in operating system and csv reader/writer
import os
import csv

#Read in the two files
buddata1 = os.path.join("budget_data_1.csv")
buddata2 = os.path.join("budget_data_2.csv")

#Set variables
Months = 0
Revenue = 0
Prev_Month = 0
Change = 0
TotalChange = 0
Max_Inc = ['',0]
Max_Dec = ['',0]


with open(buddata1, newline="") as budget:
    csvreader = csv.DictReader(budget)
    for row in csvreader:
        Months += 1
        Revenue += int(row['Revenue'])
        Change = (int(row['Revenue']) - Prev_Month)
        TotalChange = TotalChange + Change
        
        if Prev_Month != 0:
            if Change> Max_Inc[1]:
                Max_Inc[0] = row['Date']
                Max_Inc[1] = int(Change)
            elif Change< Max_Dec[1]:
                Max_Dec[0] = row['Date']
                Max_Dec[1] = int(Change)
                
        Prev_Month = int(row['Revenue'])  
       
#Print out analysis
print("")        
print("Financial Analysis")
print("-----------------")
print("Total Months: " + str(Months))
print("Total Revenue: $" + str(Revenue))
print("Average Revenue Change: $"+ str(TotalChange))
print("Greatest Revenue Increase: "+ str(Max_Inc[0])+" "+ "$" + str(Max_Inc[1]))
print("Greatest Revenue Decrease: "+ str(Max_Dec[0])+" "+ "$" + str(Max_Dec[1]))
