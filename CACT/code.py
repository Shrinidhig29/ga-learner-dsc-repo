# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data)
print(data.shape)

#Code starts here

census = np.concatenate((new_record, data), axis=0)
print(census)
print(census.shape)

age = np.array(census[:, 0])
print(age)

max_age = np.amax(age)
print(max_age)

min_age = np.amin(age)
print(min_age)

age_mean = sum(age) / len(age)
print(age_mean)

age_std = np.std(age)
print(age_std)

race_0 =  census[census[:,2]==0]
race_1 =  census[census[:,2]==1]
race_2 =  census[census[:,2]==2]
race_3 =  census[census[:,2]==3]
race_4 =  census[census[:,2]==4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

print(len_0,len_1,len_2,len_3,len_4)
minority_race = len(race_3)
print(minority_race)

senior_citizens = census[census[:,0]>60,:]
working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len =  len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)

high = census[census[:,1]>10] 
low = census[census[:,1]<=10]
# avg_pay_high = sum(high) / len(high)
# print(avg_pay_high)

# avg_pay_low = sum(low) / len(low)
# print(avg_pay_low)

avg_pay_high = np.around(np.mean(high[:,7]),decimals=2)
print(avg_pay_high)

avg_pay_low = np.around(np.mean(low[:,7]),decimals = 2)
print(avg_pay_low)


