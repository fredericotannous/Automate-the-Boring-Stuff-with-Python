name = 'zophie a cat'
print(name[7])

newName = name[0:7] + 'the' + name[8:12]
print(newName)

spam = list(range(0, 6))
print(spam)

cheese = spam
cheese[1] = 'Hello!'
print(cheese)

def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
print(eggs(spam))
print(spam)

import copy
spam = ['a', 'b', 'c']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(spam, cheese)