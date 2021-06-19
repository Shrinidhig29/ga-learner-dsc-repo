# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file


#Creating a new variable to store the value counts
loan_status = data.Loan_Status.value_counts()

#Plotting bar plot
data["Loan_Status"].value_counts().plot(kind='bar')

print(data.iloc[25,1]) 
print(data.iloc[53,9]) 
print(loan_status[0]) 
print(loan_status[1])

# Step 2
#Plotting an unstacked bar plot
property_and_loan = data.groupby(['Property_Area','Loan_Status'])
property_and_loan =  property_and_loan.size().unstack()
 
property_and_loan.plot.bar(stacked=False) 
#Changing the x-axis label
plt.xlabel('Property Area')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation='45')
plt.show()


print(property_and_loan['N'][1])
print(property_and_loan['Y'][0])

# Step 3
#Plotting a stacked bar plot
education_and_loan = data.groupby(['Education','Loan_Status'])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot.bar(stacked=True)

#Changing the x-axis label
plt.xlabel('Education Status')

#Changing the y-axis label
plt.ylabel('Loan Status')

#Rotating the ticks of X-axis
plt.xticks(rotation=45)
plt.show()

print(education_and_loan['N'][1])
print(education_and_loan['Y'][0])

# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate = data[data['Education']=='Graduate']

#Subsetting the dataframe based on 'Education' column
not_graduate = data[data['Education']=='Not Graduate']

#Plotting density plot for 'Graduate'
graduate.LoanAmount.plot(kind='density', color='green',label='Graducate')

#Plotting density plot for 'Graduate'
not_graduate.LoanAmount.plot(kind='density', color='red', label='Not Graducate')

#For automatic legend display
plt.legend()

# Step 5
#Setting up the subplots
# fig, ax_1 = plt.subplots(nrows=3, ncols=1)
fig, (ax_1,ax_2,ax_3) = plt.subplots(nrows = 3 , ncols = 1)

#Plotting scatter plot
plt.scatter('ApplicantIncome', 'LoanAmount')

#Setting the subplot axis title
plt.title('Applicant Income')

#Plotting scatter plot
plt.scatter('CoapplicantIncome', 'LoanAmount')

#Setting the subplot axis title
plt.title('CoapplicantIncome')

#Creating a new column 'TotalIncome'
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

#Plotting scatter plot
plt.scatter('TotalIncome', 'LoanAmount')

#Setting the subplot axis title
plt.title('Total Income')
plt.show()


