users = {}

users['buddy'] = 'password'
users['bolter'] = 'dylan'

print(users)
print(users['buddy'])
print('buddy' in users)

for user in users:
    print(user)