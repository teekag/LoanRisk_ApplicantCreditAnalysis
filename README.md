# LoanRisk_LendingClub
LendingClub, headquartered in San Francisco, California, is a pioneering peer-to-peer lending company in the United States. Renowned for its innovative approach, it was the first to register its offerings as securities with the Securities and Exchange Commission (SEC) and introduce loan trading on a secondary market.

# Purpose
The purpose of this repo is to document risk analysis performed in Kaggle with regards to consumer loan offerings. The risk analysis was perfromed to classify applicants, and predict their value to the loan issuer. This project is aimed at reducing rejected applicants who could provide value, and reduce accpeting unreliable borrower due to risk. Additionally, this project will help identify the types of features used in model predicts. The hypothesis of the feature selection challenge is that there are two broad categories - Firstly, features related to the applicant (demographic variables such as occupation, employment details etc.) Secondly, features related to loan characteristics (amount of loan, interest rate, purpose of loan etc.)


# Introduction
LendingClub, headquartered in San Francisco, California, is a pioneering peer-to-peer lending company in the United States. Renowned for its innovative approach, it was the first to register its offerings as securities with the Securities and Exchange Commission (SEC) and introduce loan trading on a secondary market. As the world's largest peer-to-peer lending platform, LendingClub presents a compelling case study to explore real-world business challenges addressed through exploratory data analysis (EDA) and machine learning. This study delves into risk analytics within banking and financial services, illuminating how data insights are leveraged to mitigate financial risks associated with customer lending.

# Loan Analysis Problem Statement

As an "employee" of LendingClub, you're immersed in a dynamic environment focused on providing diverse loan products to urban customers. Each loan application triggers critical decisions, balancing two key risks:

1) Loss of Business: Denying a loan to a creditworthy applicant results in missed business opportunities.
2) Financial Exposure: Approving a loan to a potentially unreliable borrower risks financial losses through defaults.

The dataset at hand comprises historical loan applicant information, including default status. The primary objective is to uncover predictive patterns indicative of default likelihood. Insights derived from these patterns can inform strategic actions such as loan denial, risk-adjusted interest rates, or tailored loan amounts.

When evaluating loan applications, two outcomes are possible:

Outcome A: Loan Accepted: The applicant is approved, leading to three potential scenarios:
- Fully Paid: Applicant fulfills all repayment obligations.
- Current: Applicant is actively repaying the loan, with no default status.
- Charged-off: Applicant defaults by failing to meet repayment obligations over an extended period.

Outcome B: Loan Rejected: The applicant does not meet eligibility criteria, and no transactional history exists for these individuals in the dataset.

# Business Objectives
LendingClub operates as a prominent online loan marketplace, facilitating personal, business, and medical financing loans. A key challenge faced by the company, like many in the lending sector, is mitigating credit losses stemming from defaults. Credit loss represents the financial impact incurred when borrowers default on their obligations, constituting a significant risk to lenders. Identifying and mitigating risks associated with 'risky' loan applicants is paramount to reducing credit losses.

The overarching objective of this case study is to leverage EDA and machine learning to identify factors driving loan defaults. By discerning strong indicators of default, known as driver variables, LendingClub aims to enhance portfolio management and risk assessment practices.

To deepen your comprehension of the domain, independent research into risk analytics is encouraged, particularly regarding variable types and their significance in predictive modeling.

LendingClub is the largest online loan marketplace, facilitating personal loans, business loans, and financing of medical procedures. Borrowers can easily access lower interest rate loans through a fast online interface.Like most other lending companies, lending loans to ‘risky’ applicants is the largest source of financial loss (called credit loss). The credit loss is the amount of money lost by the lender when the borrower refuses to pay or runs away with the money owed. In other words, borrowers who defaultcause the largest amount of loss to the lenders. In this case, the customers labelled as 'charged-off' are the 'defaulters'. If one is able to identify these risky loan applicants, then such loans can be reduced thereby cutting down the amount of credit loss. Identification of such applicants using EDA and machine learning is the aim of this case study. In other words, the company wants to understand the driving factors (or driver variables) behind loan default, i.e. the variables which are strong indicators of default. The company can utilise this knowledge for its portfolio and risk assessment. To develop your understanding of the domain, you are advised to independently research a little about risk analytics (understanding the types of variables and their significance should be enough)

# LoanStats 


| Statistic            | Description                                                                                       |
|----------------------|---------------------------------------------------------------------------------------------------|
| loan_amnt            | The listed amount of the loan applied for by the borrower. If adjusted, reflects in this value.    |
| term                 | The number of payments on the loan, expressed in months. Values are either 36 or 60.              |
| int_rate             | The interest rate on the loan.                                                                    |
| installment          | The monthly payment owed by the borrower if the loan originates.                                   |
| grade                | The loan grade assigned by LendingClub.                                                            |
| sub_grade            | The loan subgrade assigned by LendingClub.                                                         |
| emp_title            | The job title provided by the borrower during the loan application.                                 |
| emp_length           | The length of employment in years, categorized from 0 to 10, with 0 representing less than a year. |
| home_ownership       | The home ownership status provided by the borrower during registration.                            |
| annual_inc           | The self-reported annual income provided by the borrower during registration.                      |
| verification_status  | Indicates if income was verified by LendingClub, not verified, or verified from another source.    |
| issue_d              | The month in which the loan was funded.                                                           |
| loan_status          | The current status of the loan.                                                                   |
| purpose              | A category provided by the borrower for the loan request.                                          |
| title                | The loan title provided by the borrower.                                                           |
| zip_code             | The first 3 numbers of the zip code provided by the borrower in the loan application.              |
| addr_state           | The state provided by the borrower in the loan application.                                         |
| dti                  | A ratio calculated using the borrower’s total monthly debt payments on total debt obligations.      |
| earliest_cr_line     | The month the borrower's earliest reported credit line was opened.                                  |
| open_acc             | The number of open credit lines in the borrower's credit file.                                      |
| pub_rec              | The number of derogatory public records.                                                           |
| revol_bal            | The total credit revolving balance.                                                                |
| revol_util           | The revolving line utilization rate, or the amount of credit the borrower is using relative to all available revolving credit. |
| total_acc            | The total number of credit lines currently in the borrower's credit file.                           |
| initial_list_status  | The initial listing status of the loan.                                                            |
| application_type     | Indicates whether the loan is an individual application or a joint application with two co-borrowers. |
| mort_acc             | The number of mortgage accounts.                                                                  |
| pub_rec_bankruptcies | The number of public record bankruptcies.                                                          |

# Datasets

lending-club
- accepted_2007_to_2018Q4.csv.gz
- rejected_2007_to_2018Q4.csv.gz
- lending-club-20072020q1
- LCDataDictionary.xlsx
- Loan_status_2007-2020Q3.gzip

lending-club-dataset
- lending_club_loan_two.csv

lending-club-first-dataset
- loan.csv
- lending-club-loan-data-csv
- LCDataDictionary.xlsx
- loan.csv


lendingclub-issued-loans
- lc_2016_2017.csv
- lc_loan.csv
- new.html
- us-state-codes.csv



# Technologies Used
- 1450.3s - GPU P100
- pandas
- Matplotlib
- NumPy
- Seaborn
- Binary Classification - XGBOOST
- TensorFlow
- SciPy
