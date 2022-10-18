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

def save_csv(csvpath, data): 
    """Saves data from a path and data provided. 
    
    Args:
        csvpath (Path): The csv file path
        
        data: The data you want read
    
    """
             
    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
    
    with open(csvpath, 'w', newline = '') as csvfile:
            
        csvwriter = csv.writer(csvfile, delimiter=",")
        csvwriter.writerow(header)
        csvwriter.writerows(data)
        