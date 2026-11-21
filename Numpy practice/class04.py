import numpy as np
month=[22,33,45,67,70,79,80,50]
sales=np.array(month)
print(sales.dtype)
#float data type
a=np.array([12.3,44.5,66.6,45,6])
print(a.dtype)
#boleean
l=True,False,True,False
b=np.array(l)
print(b.dtype)
#string type konta bro letter
B=np.array(["Jhorna","Jannatul","Samanta"])
print(B.dtype,B.size)
#size making
a=np.array([22,44,54,64,43,54,76,86])
print(a.size)
#Practice 
list=[22,33,44,55,66,23,45]
array=np.array(list)
print(array.dtype,array.size)
#practice 2
chr=np.array(["Dhaka","Mohammedpur","Savar"])
print(chr.dtype)
