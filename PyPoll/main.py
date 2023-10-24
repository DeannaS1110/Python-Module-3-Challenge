# Import modules
import csv

# Capture path in varible
budget_csv = os.path.join('UCI Bootcamp 2023','Module 3','Resources','PyPoll','Resources','election_data.csv')

# Initialize variables  
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Open and Read CSV file
with open(csv_file, "r") as file:
         csvreader = csv.reader(file)

         # Skip the header row 
         next(csv_reader)

         # Loop through each row in the CSV 
         for row in csv_reader:
                    # Count total votes
                    total_votes += 1

                    # Get the candidate's name from the row
                    candidate_name = row[2]

                    # Check if the candidate is already in candidate dictionary
                    if candidate_name in candidates:
                                candidates[candidate_name] += 1
                    else:
                                # If not, add the candidate to dictionary and set vote count to 1
                                candidates[candidate_name] = 1

# Initialize a variable to store the results
results = []

# Iterate through the candidates and calculate percentage of votes
for candidate, votes in cnadidate.items():
        percentage = (votes/total_votes) * 100
        results.append((candidate, votes, percentage))

# Find the candidate withthe most votes
for candidate, votes, percentage in results:
        if votes > max_votes:
                max_votes = voters
                winner = candidate

# Print results to console
print("Election Results")
print("-" * 30)
print(f"Total Votes: {total_votes}")
print("-" * 30)

for candidate, votes, percentage in results:
        print(f"{candidate}: {percentage:.3f}")

print("-" * 30)
print(f"Winner: {winner}")
print("-" * 30)

# Define output file path 
output_file = "election_results.txt"

# Open the file and write results to it
with open(output_file, "w") as file:
        file.write("Election Results\n")
        file.write("-" * 30 + "\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("-" * 30 + "\n")

        for candidate, votes, percentage in results:
                file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        file.write("-" * 30 + "\n")
        file.write(fWinner: {winner}\n")
        file.write("-" * 30 + "\n")

