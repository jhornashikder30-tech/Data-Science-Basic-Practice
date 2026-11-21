#Shape -reshape
import numpy as np
Employee_Code=np.array([92831,78213,98218,98231,92316])
print(Employee_Code.shape)
#Shape -row colum
a=np.array([[77,67,87,20,40],
            [33,45,44,56,75],
            [23,43,54,65,67]])
print(a.shape)
#2nd Shape -row colum
b=np.array([[33,35,67,80],[45,67,86,90]])
print(b.shape)
#3rd shape-row colum
Employee_Information=np.array([["Nayem Islam Sagor","Nowsara Begum","Renuka"],
                               [98283,98987,98820]])
print(Employee_Information.shape)
#copy 
list=np.copy(Employee_Code)
print(list)
#2nd copy
list2=np.copy(a)
print(list2)
