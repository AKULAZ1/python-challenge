# Open CSVFile as a readable file 
import os
import csv

csvFilePath = os.path.join("Resources", "budget_data.csv")
with open(csvFilePath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")

    #Store Header Row in csvFile
    csvHeader = next(csvReader)
    #Store first row of data in csvFile
    csvFirstMonth = next(csvReader)

    Total_Months = 0
    PL_Total = 0
    Last_PL = 0
    PL_Changes = []
    PL_Change_Sum =0
    GI_Month = ""
    GI = 0
    GD_Month = ""
    GD = 0


    #Collect information in first row of csvFile and store in specified variables
    Total_Months += 1
    PL_Total = int(csvFirstMonth[1])
    #Store the Profit/Loss of the prior row to calcuate monthly changes in Loop
    Last_PL = int(csvFirstMonth[1])

    for row in csvReader:
        #For each row,
        # add 1 to the "Total_Months" and add the Profit/Loss of each month to calculate the Net Total
        Total_Months += 1
        PL_Total += int(row[1])
        #calculate all the P/L Net Change- (Current-Prior Month's)
        #sum all the foregoing changes to calculate the Total Net Change
        #add each P/L Net Change to a list 
        PL_Change = int(row[1]) - Last_PL
        PL_Change_Sum += ((int(row[1])) - Last_PL)
        PL_Changes.append(int(row[1]) - Last_PL)

        #Conditionals to determine the greatest increase and greatest decrease in profits
        #Variables to store respective months and amounts 
        if PL_Change > GI:
            GI_Month = row[0]
            GI = PL_Change

        if PL_Change < GD:
            GD_Month = row[0]
            GD = PL_Change

        #update the Last_PL to reflect the current row
        Last_PL = int(row[1])

#Calculate Average of Net Changes Over Time
PL_AOT = PL_Change_Sum / len(PL_Changes)

#Print Output in Terminal
print("\nFinancial Analysis")
print("\n----------------------------")
print(f"\nTotal Months: {Total_Months}")
print(f"\nTotal: ${PL_Total}")
print(f"\nAverage Change: ${PL_AOT:.2f}")
print(f"\nGreatest Increase in Profits: {GI_Month} (${GI})")
print(f"\nGreatest Decrease in Profits: {GD_Month} (${GD})")

#Open new Text File to display Output
textFilePath = "../PyBank/Analysis/Output.txt"
#Write in Output.txt. 
# The code to write in a text file was sourced from an Ask Python Article- Python- Print to File. 
# The link can be  found here: https://www.askpython.com/python/built-in-methods/python-print-to-file
with open(textFilePath, "w") as F:
    F.write("\nFinancial Analysis")
    F.write("\n----------------------------")
    F.write(f"\nTotal Months: {Total_Months}")
    F.write(f"\nTotal: ${PL_Total}")
    F.write(f"\nAverage Change: ${PL_AOT:.2f}")
    F.write(f"\nGreatest Increase in Profits: {GI_Month} (${GI})")
    F.write(f"\nGreatest Decrease in Profits: {GD_Month} (${GD})")
