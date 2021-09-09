import os
path = 'C://Users//Frederico//Desktop//python//Automate the Boring Stuff with Python//Section 6'
os.chdir(path)
spam = ['cat', 'bat', 'rat', 'elephant']

spam_2 = [['cat', 'elephant'], [10,20,30,40]]
print(spam_2)
print(spam_2[0])
print(spam_2[0][0])
print(spam_2[1][2])

spam_3 = ['cat', 'bat', 'rat', 'elephant', 'artur']
print(spam_3[-1])
print(os.getcwd())
print(spam_3[1:4])

spam_4 = [10, 20, 30]
spam_4[1] = 'hello'
print(spam_4)

spam_4[1:3] = ['cat', 'dog', 'frederico']
print(spam_4)

spam_5 = ['cat', 'dog', 'butter', 'milk']
print(spam_5[:2])
print(spam_5[1:])

print(len(spam_5))
print(list('Hello'))

print('cat' in spam_5)
print('cat' not in spam_3)