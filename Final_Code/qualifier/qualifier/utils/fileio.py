# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Read the CSV data
        for row in csvreader:
            data.append(row)

        header=data[0]
        n=len(data)
        data=data[1:n]
    return data, header


def save_csv(csvpath, data, header):
    print (f"Type csvpath {type(csvpath)}")

    #print(f"This is the input data: {data}")
    #print(f"Tghis is the header: {header}")    
    #print(f"This is the path {csvpath}, and the type: {type(csvpath)}")

    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Export the header
        csvwriter.writerow(header)

        # Write the CSV data
        for row in data:
            csvwriter.writerow(row)
    return(csvfile)

def csv_path_to_file_from_string_dir(string_dir, csv_output_file_name="output.csv"):
    """
    This function receives a string as a directory path, and the name of a csv file,
    and return the corresponding file path. 
    If the directory does not exist, it creates it.
    """

    # Set the output file path
    file_path = Path(string_dir)
    file_path.mkdir(parents=True, exist_ok=True)

    output_file=csv_output_file_name
    output_path= file_path/output_file

    csvpath = Path(output_path)
    return(csvpath)

