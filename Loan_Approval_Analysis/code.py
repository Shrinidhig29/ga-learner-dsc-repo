# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
# bank = pd.read_csv(path)
categorical_var = bank_data.select_dtypes(include='object')
# print(categorical_var)
print(categorical_var.shape)

numerical_var = bank_data.select_dtypes(include='number')
# print(numerical_var)
print(numerical_var.shape)

banks = bank_data.drop(['Loan_ID'], axis=1)
print(banks.shape)
print(banks.isnull().sum())

bank_mode = banks.mode().iloc[0]
print(bank_mode)

banks.fillna(bank_mode, inplace=True)


avg_loan_amount =  banks.pivot_table(values=["LoanAmount"], index=["Gender","Married", "Self_Employed"],aggfunc=np.mean)

avg_loan_amount['LoanAmount'][1]

loan_approved_se = banks[(banks["Self_Employed"]=="Yes") & (banks["Loan_Status"]=="Y")].count()
print(loan_approved_se)

loan_approved_nse=banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].count()
print(loan_approved_nse)

Loan_Status = 614

percentage_se =((loan_approved_se*100) / 614)
print(percentage_se)

percentage_nse =((loan_approved_nse*100) / 614 )
print(percentage_nse)

loan_term = banks['Loan_Amount_Term'].apply(lambda x :int(x)/12)
print(loan_term)
big_loan_term = banks[loan_term>=25]

col_to_show = ['ApplicantIncome','Credit_History'] 
loan_groupby = banks.groupby(['Loan_Status'])
mean_values = loan_groupby.agg([np.mean])
print(mean_values.iloc[1,0], 2)

#Code starts here




