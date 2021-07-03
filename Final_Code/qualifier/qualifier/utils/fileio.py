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

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(csvpath, data, header):
    print (f"Type csvpath {type(csvpath)}")

    #print(f"This is the input data: {data}")
    #print(f"Tghis is the header: {header}")    
    print(f"This is the path {csvpath}, and the type: {type(csvpath)}")

    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Export the header
        csvwriter.writerow(header)
        print("ya escribi el header")

        # Write the CSV data
        for row in data:
        #    print(f"escribi una linea {row}")  BORRAR ESTA LINEA
            csvwriter.writerow(row)
    return(csvfile)

def csv_path_to_file_from_string_dir(string_dir, csv_output_file_name="output.csv"):
    """
    This function receives a string as a directory path, and the name of a csv output file,
    and return the path to that file located in tht directory.
    If the directory does not exist, it creates it.
    """

    # Set the output file path
    file_path = Path(string_dir)
    file_path.mkdir(parents=True, exist_ok=True)

    output_file=csv_output_file_name
    output_path= file_path/output_file

    csvpath = Path(output_path)
    return(csvpath)