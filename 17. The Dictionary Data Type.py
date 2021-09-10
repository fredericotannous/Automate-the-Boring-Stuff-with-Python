myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])

spam = {12345:'luggage combination', 'answer': 42}

eggs = {'name': 'zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'age': 8, 'name': 'zophie'}
print(eggs == ham)

print('name' in eggs)

print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

for k in eggs.keys():
    print(k)

for k, v in eggs.items():
    print(k, v)

print('cat' in eggs.values()) 

eggs.get('age', 0)
print(eggs.get('color', ''))

picnickIntems = {'apples': 5, 'cups':2}
print('I am bringing ' + str(picnickIntems.get('napkins', 0)) + ' to the picknick')

print(eggs.setdefault('color', 'black'))
print(eggs)



message = 'It was a bright cold day in April, and the clocks were strinking thirteen.'
count = {}
import pprint
for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)