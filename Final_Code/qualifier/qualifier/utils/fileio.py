# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


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


def export_csv(csvpath, data, header):
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
            print(f"escribi una linea {row}")
            csvwriter.writerow(row)
    return(csvfile)