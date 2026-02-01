import numpy as np


#1d

salaries=np.array([20000,18000,20000,40000,35000,50000,45000])
experience=np.array([1,3,2,1,3,3,2])

#print highest salary
print("highest salary",np.max(salaries))

#index of highest salary
print("index of salary",np.argmax(salaries))


#print salary>30000
#boolean masking
#<,>,==,>=,<=,!=

high_salary=salaries[salaries>30000]
print("salary >30k",high_salary)

greater_equal = salaries[salaries >= 35000]
print("Salary >= 35k :", greater_equal)

less_equal = salaries[salaries <= 20000]
print("Salary <= 20k :", less_equal)

not_equal = salaries[salaries != 40000]
print("Salary != 40k :", not_equal)



#print salary <20000
low_salary=salaries[salaries<20000]
print("salary <20k",low_salary)

#print salary==20000
exact_salary=salaries[salaries==20000]
print("exact salary",exact_salary)

#print total number of emp who have 20k salary
print(len(exact_salary))
print(exact_salary.size)

#-------multiple conditions

eligible_for_promotion=salaries[(salaries>250000)&(experience>2)]
print("eligible for_promotion",eligible_for_promotion)

#where

bonus=np.where(salaries>30000,5000,2000)
print("bonus",bonus)

updated_salary=np.where(salaries<30000,30000,salaries)
print(updated_salary)

finalsalary=salaries+bonus
print(finalsalary)

salary_data=salaries[(salaries>20000) &(salaries<40000)]

print("data",salary_data)
print("max salary from 20k to 40k is:",np.max(salary_data))
print("index",np.argmax(salary_data))
