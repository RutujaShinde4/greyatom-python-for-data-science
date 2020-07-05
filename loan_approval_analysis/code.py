# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
banks = pd.read_csv(path)
categorical_var = banks.select_dtypes(include = 'object')
print(categorical_var.head(5))
print("Shape of categorical variable is",categorical_var.shape)
numerical_var = banks.select_dtypes(include = 'number')
print(numerical_var.head(5))
print("Shape of numerical variable is",numerical_var.shape)
banks = banks.drop(columns="Loan_ID")
print(banks.head(5))
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
print(bank_mode)

banks.fillna(bank_mode,inplace=True)
print(banks.isnull().sum())

avg_loan_amount = banks.pivot_table(index =["Gender","Married","Self_Employed"],values =["LoanAmount"],aggfunc = np.mean)
print(avg_loan_amount)
loan_approved_se = banks.loc[(banks["Self_Employed"]=="Yes") & (banks["Loan_Status"] == "Y"),["Loan_Status"]].count()
print(loan_approved_se)
loan_approved_nse = banks.loc[(banks["Self_Employed"]=="No") & (banks["Loan_Status"] == "Y"),["Loan_Status"]].count()
print(loan_approved_se)
percentage_se = (loan_approved_se *100/614)
print(percentage_se)
percentage_nse = (loan_approved_nse *100/614)
print(percentage_nse)

loan_term = banks["Loan_Amount_Term"].apply(lambda x: int(x)/12)
big_loan_term =  len(loan_term[loan_term]>=25)
print(big_loan_term)
loan_groupby = banks.groupby(["Loan_Status"])
loan_groupby = loan_groupby["ApplicantIncome","Credit_History"]
mean_values = loan_groupby.agg([np.mean])
print(mean_values)






