#1st
from functools import reduce
nums=[1,2,3,4,5,6,7,8,9,0]
even=list(filter(lambda e:e%2==0,nums))
double=list(map(lambda d:d*2,even))
sums=reduce(lambda a,b:a+b,double)
print(nums)
print(even)
print(double)
print(sums)
print("Done!!")
#2nd
a=int(input("a:"))
b=int(input("b:"))
_max=lambda a,b:print("max value is : ",a) if a>b else print("max value is : ",b)
_max(a,b)
#3rd
name=["praVeen","kumAr","lR","vijaY","thalaPathI"]
ar=list(map(lambda n:str.title(n),name))
print(ar)
