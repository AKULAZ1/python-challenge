# Open CSVFile as a readable file 
import os
import csv

csvFilePath = os.path.join("Resources", "election_data.csv")
with open(csvFilePath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter = ",")

    #Store Header Row in csvFile
    csvHeader = next(csvReader)

    Total_Votes = 0

    Candidates = []

    Votes = {}

    for row in csvReader:
        # For each row in the csvFile,
        # Add one to the Total_Votes cast
        Total_Votes += 1

        #Determine whether the candidate is already in the "Votes" Dictionary
        #If so, add 1 to his/her vote count; if not, add him/her to the "Candidates" list, the "Votes" Dictionary, and add 1 to his/her value in the dictionary.
        if row[2] in Candidates:

            Votes[str(row[2])] += 1
        else:
            Candidates.append(row[2])
            Votes[str(row[2])] = 1

    Votes_List =[]
    Share_List = []
    Last_Value = 0

    for key in Votes:
        #For each key [Candidate Name] in the "Votes" Dictionary.
        #Add that Candidates' votes to "Votes_List"
        #Calculate what percentage of the total votes they received 
        #Add that percentage to the "Share_List"
        Votes_List.append(int(Votes[key]))
        Share = (int(Votes[key])/int(Total_Votes))*100
        Share_List.append(Share)

        #Determine whether his/her share of the votes is the greatest- Who is the winner?
        if int(Votes[key]) > int(Last_Value):
            Winner = key
            #Update Last_Value to hold Votes of temporary "Winner" until Loop ends
            Last_Value = int(Votes[key])
    
    print("\nElection Results")
    print("\n----------------------------")
    print(f"\nTotal Votes: {Total_Votes}")
    print("\n----------------------------")
    print(f"\n{Candidates[0]}: {Share_List[0]:.3f}% ({Votes_List[0]})")
    print(f"\n{Candidates[1]}: {Share_List[1]:.3f}% ({Votes_List[1]})")
    print(f"\n{Candidates[2]}: {Share_List[2]:.3f}% ({Votes_List[2]})")
    print("\n----------------------------")
    print(f"\nWinner: {Winner}")
    print("\n----------------------------")
    
    #Open new Text File to display Output
    textFilePath = "../PyPoll/Analysis/Output.txt"
    #Write in Output.txt. 
    # The code to write in a text file was sourced from an Ask Python Article- Python- Print to File. 
    # The link can be  found here: https://www.askpython.com/python/built-in-methods/python-print-to-file
    with open(textFilePath, "w") as F:
        F.write("\nElection Results")
        F.write("\n----------------------------")
        F.write(f"\nTotal Votes: {Total_Votes}")
        F.write("\n----------------------------")
        F.write(f"\n{Candidates[0]}: {Share_List[0]:.3f}% ({Votes_List[0]})")
        F.write(f"\n{Candidates[1]}: {Share_List[1]:.3f}% ({Votes_List[1]})")
        F.write(f"\n{Candidates[2]}: {Share_List[2]:.3f}% ({Votes_List[2]})")
        F.write("\n----------------------------")
        F.write(f"\nWinner: {Winner}")
        F.write("\n----------------------------")




            





