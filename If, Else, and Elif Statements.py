name = 'Alice'
if name == 'Alice':
    print('Hi, Alice')
print('Done')

password = 'swordfish'
if password == 'lol':
    print('Access granted')
else:
    print('Wrong password.')

name = 'bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print("You're not Alice, kiddo.")
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire.")
elif age > 100:
    print("You're not Alice, grannie.")

print("Enter a name.")
name = input()
if name:
    print("Thank you for entering your name.")
else:
    print("You did not enter a name.")