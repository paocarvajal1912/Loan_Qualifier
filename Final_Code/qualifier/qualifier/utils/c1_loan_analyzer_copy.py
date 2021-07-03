# Basic Tools for Loan Portfolio Analysis in Python
# Type of Loans: Bullet with Monthly Interest Payment Schedule
# Applied to a list of dictionaries

#Python libraries & modules involved: pathlib, Path, csv
#Python version: 3.0 or higher for the use of f-strings

# Code by: Paola A. Carvajal Almeida
# paola.antonieta@gmail.com
# (C1) ucb-virt-fin-pt-06-2021-u-b


from fileio import export_csv
import csv
from pathlib import Path

print('\033c') # Cleaning Terminal screen
"""Part 1: Automation of Simple Calculations.

This code automate aggregation calculations for a loan portfolio with pricing data and display on screen.

Example shows calculations on a list of prices for 5 individual loans.
    1. Uses the `len` function to calculate the total number of loans in the list.
    2. Uses the `sum` function to calculate the aggregated price of all loans in the list.
    3. Uses 1.& 2. to calculate the average loan price.
    4. Print all calculations with descriptive messages using f-string.
"""
loan_costs = [500, 600, 200, 1000, 450]

# `len` function calculates the total number of loans in the list.
print("1. LOAN DATA SUMMARY")
total_number_of_loans=len(loan_costs)
print (f"Total number of loans: {total_number_of_loans}")

# Uses `sum` function to calculate the price of the portfolio of all individual loans in the list.
total_value_of_loans=sum(loan_costs)
print(f"Current market value of the portfolio of individual loans: ${total_value_of_loans:,.2f}")

# Average loan amount from the list?
average_loan_amount=total_value_of_loans/total_number_of_loans
print(f"Average loan price is: ${average_loan_amount:,.2f} \n\n")

"""Part 2: Code to Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of the above loans, here are the steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost (price in this case), then recommend to buy plua a proper explanation
    b. Else, the present value of the loan is less than the loan cost, then recommend NOT TO BUY and print a proper explanation
"""

# Given loan data it calculates the present value for the loan
# A bullet loan has the payment of the principal at maturity.
# This loan pays interest monthly
loan = {
    "loan_price": 500, 
    "remaining_months": 9,
    "repayment_interval": "bullet",  
    "future_value": 1000,
}

# Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
print ("2. ANALISIS OF LOAN DATA: VALUATION AND PURCHASE RECOMMENDATION")
future_value_loan     = loan.get("future_value")
remaining_months_loan = loan.get("remaining_months")

print(f"Future value of the loan: ${future_value_loan:,.2f}")
print(f"Remaining months of the loan: {remaining_months_loan}")


# Calculation of FAIR VALUE using Present Value and monthly capitalization
# Uses a minimum required annual return of 20% as the discount rate.
# Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
required_minimum_discount_rate_annual=0.2
fair_value_loan= future_value_loan/(1+required_minimum_discount_rate_annual/12)**remaining_months_loan  #OBS the exponent will apply just to the denominator

# Conclusions of the analysis.
#  Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, provide recommendation to buy, and provide proper explanation
#    Else, the present value of the loan is less than the loan cost, then it provides recommendation NOT TO BUY, and provide proper explanation

loan_price=loan.get("loan_price")
print(f"Fair value of the loan: ${fair_value_loan:,.2f}")
print(f"Loan price: ${loan_price:,.2f}")

if fair_value_loan>=loan_price:   
    print(f"The loan is worth at least the cost to buy it.")
    if fair_value_loan>loan_price:
        print(f"Recommendation: BUY, because the loan is cheaper or very close to its fair value at your minimum discount rate of {required_minimum_discount_rate_annual*100:.1f}%. \n\n")
else:
    print("The loan is too expensive and does not worth the price.")
    print("Recommendation: DO NOT BUY \n\n")


"""Part 3: Code to Perform Financial Calculations.

Performs financial calculations using functions. The code is made to:

1. Define a function to calculate present value.
    a. This function includes parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function return the `present_value` for the loan.
2. Use of the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Loan to be evaluated
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Code defines a function that calculates present value.
#    Parameters: `future_value`, `remaining_months`, and the `annual_discount_rate`
#    Function returns the `present_value` for the loan.
print("3. FINANCIAL CALCULATIONS USING FUNCTIONS")
def present_value(future_value, remaining_months, annual_discount_rate):
    present_value=future_value/(1+annual_discount_rate/12)**remaining_months
    return(present_value)


# Code uses the function to calculate the present value of the new loan.
#    It uses an `annual_discount_rate` of 0.2 for this new loan calculation.
investor_annual_discount_rate=0.2
present_value_new_loan=present_value(new_loan["future_value"], new_loan["remaining_months"], investor_annual_discount_rate)
print(f"Present value of the new loan: ${present_value_new_loan:,.2f} \n\n")


"""Part 4: Code conditionally filters lists of loans.

In this section, the code uses a loop to iterate through a series of loans and select only the inexpensive loans.
Steps:
1. Create a new, empty list called `inexpensive_loans`.
2. Use 1. for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list called `inexpensive_loans`
inexpensive_loans=[]

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    price_of_unclassified_loan=loan["loan_price"]
    if price_of_unclassified_loan<=500:
        inexpensive_loans.append(loan)


# Print the `inexpensive_loans` list
# Code applies an iteration so the format is readable
print("4. SELECTION OF INEXPENSIVE LOANS:")

for loan in range(0,len(inexpensive_loans)):
    for key, value in inexpensive_loans[loan].items():
        print(f"[{loan}] {key} : {value} ")
    print('\n')


"""Part 5: Saving results.

Code to generate an output with this list of inexpensive loans to a csv file. Steps:
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Reference to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]
data = [[200, 300, 400, 500]]



export_csv(csvpath,data, header)

# # Use the csv library and `csv.writer` to write the header row
# # and each row of `loan.values()` from the `inexpensive_loans` list.
# with open(output_path, 'w', newline='') as csv_output_inexpensive_loans_file:
#     csvwriter=csv.writer(csv_output_inexpensive_loans_file) # creates writer
#     csvwriter.writerow(header)                              # writer writes header row
#     count=0
#     for row in inexpensive_loans:                           #iteneration goes row by row
#         csvwriter.writerow(row.values())
#         count+=1
 #   print(f"\n Data regarding loans classified as inexpensive have been exported to a csv file in the following path:\n {output_path.absolute()} \n\n")
        


