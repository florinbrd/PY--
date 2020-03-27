# Question 3: Accept string from the user and display only those characters which are present at an even index

def even_char(string_defined):
    print(f'Your original string is: {string_defined}')
    for item in range(0, len(string_defined)-1, 2):
        if item % 2 == 0:
            print("index[", item,"]", string_defined[item] )


word = str(input('Enter your string: '))

even_char(word)
