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
    """Save data with header as an output on a CSV file in the csvpath provided.

    Args:
        csvpath: The csv file-path where the data will be saved
        data: a list of lists with data
        header: a proper header for the data parameter

    Returns:
         The csvpath to the file with the data output
    """
    print (f"Type csvpath {type(csvpath)}")

    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Export the header
        csvwriter.writerow(header)

        # Write the CSV data in the csvfile
        for row in data:
            csvwriter.writerow(row)
    print(f"\n Data has been exported to the following path:\n {csvpath.absolute()} \n\n")
    return(csvpath)

