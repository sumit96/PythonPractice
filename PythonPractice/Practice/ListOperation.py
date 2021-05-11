'''
Created on 12-May-2021

@author: sumitpuri
'''

num = [3,20,30,10,1]
print(num)

num = ['Sumit','Amit','Puri']
print(num)

num=[1.2,'Sumit',29]
print(num)

numNew= ["Amit",3,0.3]
print(numNew)

addList = [num, numNew]
print(addList)

sub= num[2:]
print(sub)

num.append("object")
print(num)

num.insert(2, 'InsertNew')
print(num)

num.remove('object')
print(num)

num.pop(2)
print(num)

del num[1:]
print(num)

num.extend(['test',4])
print(num)


print(min(num))

newData=[2,39,12,30,1]
num.sort()
print(num)
