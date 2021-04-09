# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)

#Code starts here
census=np.concatenate((new_record,data),axis=0)
print(census.shape)

#subsetting the array to include only 'age' column
age=census[:,0]
#finding max value of age
max_age=np.max(age)
print("Max Age:",max_age)
#finding min value of age
min_age=np.min(age)
print("Min Age:",min_age)
#find mean of age
age_mean=np.mean(age)
print("Age Average:",age_mean)
#find standard deviation of age
age_std=np.std(age)
print("Standard deviation of age:",age_std)

#subsets of Race
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]

#length of subsets
len_0=len(race_0)
print(len_0)
len_1=len(race_1)
print(len_1)
len_2=len(race_2)
print(len_2)
len_3=len(race_3)
print(len_3)
len_4=len(race_4)
print(len_4)

#minority race
minority_race=len(race_3)
print("Minority Race:",minority_race)

#finding senior citizens
senior_citizens=census[census[:,0]>60]
working_hours_sum=senior_citizens.sum(axis=0)[6]
print("Working hours :",working_hours_sum)

#finding length 
senior_citizens_len=len(senior_citizens)

#average working hours
avg_working_hours=working_hours_sum/senior_citizens_len

print("Average working hours of senior citizens:",avg_working_hours)

#finding average high and low pay
high=census[census[:,1]>10]
low=census[census[:,1]<=10]


avg_pay_high=np.mean([high[:,7]])
avg_pay_low=np.mean([low[:,7]])
print("Average pay(high):",avg_pay_high)
print("Average pay (Low:",avg_pay_low)






