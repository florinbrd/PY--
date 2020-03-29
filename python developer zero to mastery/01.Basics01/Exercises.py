name = 'Florin Bordei'
age = 55
relationship_status = 'in a relationship'

relationship_status = 'it\'s complicated'
print(relationship_status)

birth_year = input('what year where you born? ')
print(birth_year)
age = 2020 - int(birth_year)
print(f'your age is : {age}')

# ___________________

username = input('username:')
password = input('password:')
password_length = len(password)
hidden_password = '*' * password_length


print(f'{username}, your password {hidden_password} is {password_length} letters long')
