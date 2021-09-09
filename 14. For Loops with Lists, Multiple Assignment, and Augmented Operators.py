#for i in range(4):
    #print(i)

print(list(range(4)))
spam = list(range(0, 100, 2))
print(spam)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

cat = ['fat', 'orange', 'loud']

size, color, disposition = cat
for i in cat:
    print(i)

a = 'AAA'
b = 'BBB'

a, b = b, a
print(a, b)

spam = 32
spam = spam + 1
print(spam)

spam +=1