from array import *

#solution:#1
array1=array('i',[1,2,3,4,5,6,7,8,9,10])
reversed_array0=array1[::-1]
print("The reverse array is"+str(array1[::-1]))


#solution:#2
reversed_array=[]
for i in range(len(array1)-1,-1,-1):
    reversed_array.append(array1[i])
print(reversed_array)

#solution:#3
reversed_array1=array1.reverse()
print(reversed_array)