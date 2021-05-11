'''
Created on 12-May-2021

@author: sumitpuri
'''

''' Round value means Tuple and its immutable and its faster than list'''

tup = (2,3,1,5,4,5)

print(tup[2])

'''returning index of 5'''
print(tup.index(5,))

'''returning number of repeat'''
print(tup.count(5))


''' Set represent in {} and it always change the sequence, processing is fast,
 does not allow duplicate, Fetch by index not allowed'''
setVal={3,9,4,2,1}
print(setVal)