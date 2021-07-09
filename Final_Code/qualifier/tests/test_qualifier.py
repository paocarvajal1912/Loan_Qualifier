# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

#def test_save_csv():
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

# def test_filters():
#     bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
#     current_credit_score = 750
#     debt = 1500
#     income = 4000
#     loan = 210000
#     home_value = 250000

#     monthly_debt_ratio = 0.375

#     loan_to_value_ratio = 0.84

#     assert filters.filter_credit_score(credit_score, bank_list)


    
#     # @TODO: Test the new save_csv code!


def test_save_csv():
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    csvpath=Path('./data/output/qualifying_loans.csv')
    header=['Lender','Max Loan Amount','Max LTV','Max DTI','Min Credit Score','Interest Rate']
    data=[
    ['Bank of Big - Premier Option',300000,0.85,0.47,740,3.6],
    ['West Central Credit Union - Premier Option',400000,0.9,0.35,760,2.7]
    ]
    print("generando el testeo")
    print(f"csvpath: {csvpath}")
    print(type(csvpath))
    assert fileio.save_csv(csvpath,data,header).exists()==True

#    save_csv(csvpath, data, header):



