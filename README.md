# Fake Customer Data Creator

This repository contains a Python script that creates a CSV file that contains faked customer contact data with missing 
values.

The data created is aimed to be used as sample data to demonstrate how powerful data quality tools are with respect 
to measuring and aggregating in the DQ dimension completeness.
Consequently, the actual values created are not important, in contrast to the missing values.
Each column has a probability of $0.2$ (i.e., $20 \\%$) to be empty in every row created, i.e., to contain a missing value.
Following this, the probability that a completely empty row is generated is $0.2^8 = 0.00000256$ (i.e., $0.000256 \\%$).

The created CSV file features the following columns:
* `CustomerID`   - Identifier of a customer
* `FirstName`    - First name of a customer
* `LastName`     - First name of a customer
* `AddressID`    - Reference to the address of an customer
* `EmailAddress` - Email address of a customer
* `Phone`        - Phone number of a customer
* `Mobile`       - Mobile phone number of a customer

To use the provided script the following steps must be followed:
* Clone the repository
* Run `pip install -r requirements.txt` in the local repository
* Run `python3 create_customer_data.py`
* The CSV file will be generated and stored to `fake_customer_data.csv` in the local repository 


As configured in the constant `NUMBER_OF_ROWS_TO_GENERATE` of the script, 10000 rows are created per default. 
In case a different number of rows should be generated, this constant must be adjusted.  
