# Importing the necessary modules 
import csv 
import json 


# Creating a function to convert a csv file to json 
def make_json(csv_file, json_file): 
    # Create a dictionary 
    data = {}; 

    # Open a csv reader called the dictreader 
    with open(csv_file, encoding="utf-8") as file: 
        csvReader = csv.DictReader(file); 

        # Convert each row into a dictionary 
        # and add it to the data 
        for rows in csvReader: 
            # Assuming a column name "No" to 
            # be the primary key 
            key = rows["Date"]
            data[key] = rows 
        

    # Open a json writer, and user the json.dumps() 
    # function to dump the data 
    with open(json_file, 'w', encoding="utf-8") as jsonfile: 
        jsonfile.write(json.dumps(data, indent=4))


# 
csv_file_path = "database.csv"; 
json_file_path = "data.json"

# Call the make json function 
make_json(csv_file_path, json_file_path); 