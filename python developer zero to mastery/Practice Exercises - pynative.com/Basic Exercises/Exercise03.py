# Question 4: Given a string and an int n, remove characters from a string starting from zero up to n and return a new string

def remove_chars(str, n):
    print(f'Your original string is {str}')
    print(f'Other solution to your modified string: {str[n:]}')


word = input('Enter your word: ')
number = int(input('Enter the number of chars to be removed: '))

remove_chars(word, number)

