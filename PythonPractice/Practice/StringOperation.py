'''
Created on 11-May-2021

@author: sumitpuri
'''
'''Adding operation'''
x = 2+2
print(x)

'''Concatenate operation'''
name = 'sumit'
name = name + ' puri'

print(name)

'''Print by position'''
char = name[3]
print(char)

char = name[-4]
print(char)

char = name[0:3]
print(char)

char = name[-4:-1]
print(char)

char = 'Hi ' + name[:6]
print(char)

char = 'I am good ' +name[6:]
print(char)

'''Size of string'''
strSize = len(name)
print(strSize)