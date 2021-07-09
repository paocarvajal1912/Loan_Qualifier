# -*- copruebaing: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
from os import lseek
import sys
import fire
import questionary
from pathlib import Path
import time


from qualifier.utils.fileio import (
    load_csv,
    save_csv
)

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size  import filter_max_loan_size
from qualifier.filters.credit_score   import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value  import filter_loan_to_value

time.sleep(1)
print('\033c')

def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a path to a sheet with the data (.csv):").ask()
    csvpath = Path(csvpath)

    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}. Please try running the App again. Make sure that the path exist. \n\n")

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt         = questionary.text("What's your current amount of monthly debt?").ask()
    income       = questionary.text("What's your total monthly income?").ask()
    loan_amount  = questionary.text("What's your desired loan amount?").ask()
    home_value   = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt         = float(debt)
    income       = float(income)
    loan_amount  = float(loan_amount)
    home_value   = float(home_value)

    return credit_score, debt, income, loan_amount, home_value


def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list)  : A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float)      : The applicant's total monthly debt payments.
        income (float)    : The applicant's total monthly income.
        loan (float)      : The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)
    return bank_data_filtered
()


def save_qualifying_loans(qualifying_loans, header):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.

    Returns no value
    """

# Acceptance criterias 
    number_of_qualifying_loans=len(qualifying_loans)
    print(f"You have {number_of_qualifying_loans} lenders for which your loan qualifies.\n\n")
 
    # Acceptance criteria 2:if no qualified loans, notify user and exit
    if number_of_qualifying_loans==0:
       sys.exit("There are no qualifying loans in the analized lenders. Thanks for using this application. Good bye.\n\n")


    output_choice=questionary.select('How would you like to see the results:', 
        choices=[
            "Display on screen the list of lenders for which the loan qualifies",
            "Export detailed results of lenders and approval conditions to a csv-file",
            "Exit"]).ask()

    if output_choice=="Display on screen the list of lenders for which the loan qualifies":
        count=1
        for list in qualifying_loans:
            print(count, list[0])
            count +=1
        print(f"\n\n")
        sys.exit("Thanks for your request.\n\n")
 
    # Acceptance criteria 3: user able to opt out of saving results
    elif output_choice=="Exit":
         sys.exit("\n You have opt to exit. Thanks for using our application.")
    
        # Acceptance criteria 4&5: prompt user for a file path to save the loan as a csv file
    else:
        path_input = questionary.text('What csv-file path you want the results to be exported? Please make sure to include the csv extention (.csv) to your file.').ask()
        file_extension=path_input[-4:].lower()
        #Make sure export file is csv
        if file_extension!='.csv':
            sys.exit(f"Your file extension do not correspond to a csv-file (.csv). We are not able to complete your request.")
        
        # Set the output file path
        csvpath=Path(path_input)

        #Verify the path exist
        if not csvpath.exists():
            sys.exit(f"\n This file does not exist currently, so it has been created. \n\n")
        # If path exist, set the output file path

        if csvpath.exists():
            print("This file currently exist, so it has been overwrited.")
        
        save_csv(csvpath, qualifying_loans, header)

    return()


def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data, header = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans, header)


if __name__ == "__main__":
    fire.Fire(run)
