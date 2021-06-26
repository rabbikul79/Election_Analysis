#1. Total number of votes cast
#Add our dependencies
import os
import csv
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
# Read and print the header row.
    headers = next(file_reader)
    print(headers)
# Close the file.
    #election_data.close()
# Create a filename variable to a direct or indirect path to the file.

# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")
#outfile = open(file_to_save, "w")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Write some data to the file.
#outfile.write("Hello World")
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")
   # Close the file
txt_file.close()
#2. A complete list of candidates who received votes

#3. Total number of votes each candidate received

#4. Percentage of votes each candidate won

#5. The winner of the election based on popular vote