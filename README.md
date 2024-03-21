# LoanRisk_LendingClub
LendingClub, headquartered in San Francisco, California, is a pioneering peer-to-peer lending company in the United States. Renowned for its innovative approach, it was the first to register its offerings as securities with the Securities and Exchange Commission (SEC) and introduce loan trading on a secondary market.

# Loan Analysis Problem Statement

# Introduction
LendingClub, headquartered in San Francisco, California, is a pioneering peer-to-peer lending company in the United States. Renowned for its innovative approach, it was the first to register its offerings as securities with the Securities and Exchange Commission (SEC) and introduce loan trading on a secondary market. As the world's largest peer-to-peer lending platform, LendingClub presents a compelling case study to explore real-world business challenges addressed through exploratory data analysis (EDA) and machine learning. This study delves into risk analytics within banking and financial services, illuminating how data insights are leveraged to mitigate financial risks associated with customer lending.

Business Understanding
As an employee of LendingClub, you're immersed in a dynamic environment focused on providing diverse loan products to urban customers. Each loan application triggers critical decisions, balancing two key risks:

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

