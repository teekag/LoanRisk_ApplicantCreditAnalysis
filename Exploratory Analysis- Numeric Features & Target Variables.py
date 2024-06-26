data['loan_status'] = data.loan_status.map({'Fully Paid':1, 'Charged Off':0})

data.corr()['loan_status'].drop('loan_status').sort_values().hvplot.barh(
    width=600, height=400, 
    title="Correlation between Loan status and Numeric Features", 
    ylabel='Correlation', xlabel='Numerical Features', 
)

# **Conclusion: Notice, there are broadly three types of features**

- Features related to the applicant (demographic variables such as occupation,employment details etc.)
- Features related to loan characteristics (amount of loan, interest rate, purpose of loan etc.)

