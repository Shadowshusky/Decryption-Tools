import csv

data = {}

with open('ransomware_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        if len(row) >= 2:
            data[row[0].lower()] = row[1]

# ask for input and search for the ransomware name
ransomware_name = input("What ransomware attack was executed on a machine? ").lower()
if ransomware_name in data:
    print(f"The link to decrypt {ransomware_name.title()} is {data[ransomware_name]}")
else:
    print("Sorry, we couldn't find that ransomware in our database.")
