# different data types: str, int, float (main ones)
# list, dict : more complex
# precedence of operators follow the same pattern and += or -=

print(2 ** 2)  # 2 to the power of 2
# different mathematical functions in py: max, min, abs, round etc.

# string concatenation 'hello' + 'florin'
# to check the type of a variable use type

print(type('hello'))

# variable conversion

print(int(2.2))

# escape sequence: use \ to continue the string
# \t and \n like in java

weather = 'it is sunny'
print(weather)

# formatted strings
name = 'john'
age = 55
print(str(age))
print(f'hi {name}, you are {age} years old')

print('hi {}. You are {} years old.'.format('Johnny', '55'))
print('hi {}. You are {} years old.'.format(name, age))
print('hi {0}. You are {1} years old.'.format(name, age))
print('hi {new_name}. You are {new_age} years old.'.format(new_name='Sally', new_age=100))

# string indexes

selfish = 'FlorinDeLaGalati'
print(selfish[0])
print(selfish[1])
# to set a start and an end
print(selfish[0:5])

print(selfish[0:7:2])  # step over

print(selfish[:5])  # default 0

print(selfish[-1])  # starts at the end of the string

print(selfish[2:])  # prints starting with the second position 

print(selfish[::-1])  # we get the reverse of the string

# immutability
# strings are immutable, cannot be changed
# strings can be reassigned
# we cannot change the value of selfish[0] = 0 so we need to complete reassign the value
# what we can do is:

selfish = selfish + '8'
print(selfish)

# built in function methods
# str() int() float() print() type() abs() round() + more online
# len() we can use it for strings but it does not starts from 0, it goes from 1

print(len('Florin'))

greet = 'helloooooo'
print(greet[:])
print(greet[0:len(greet)])
print(greet[1:len(greet)])

quote = 'to be or not to be'
print(quote.upper())
print(quote.lower())
print(quote.capitalize())
print(quote.find('be'))  # finds the index where it starts
print(quote.replace('be', 'me'))  # replaces the occurrence of be, we just overwrite them in this case
print(quote)

# we can just create a new string with the replace

quote2 = quote.replace('be', 'me')
print(quote2)

# booleans

name = 'Florin'
is_cool = True
print(is_cool)
print(type(is_cool))


# list
# ordered sequence of objects, of any type
# same like an array

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

amazon_cart = ['notebook', 'sunglasses']
print(amazon_cart[0])
print(amazon_cart[1])

# list slicing

amazon_cart1 =[
    'notebooks',
    'sunglasses',
    'apples',
    'oranges'
]

print(amazon_cart1[0::2])

# lists are mutable
amazon_cart1[0] = 'laptop'
new_cart = amazon_cart1[0:3] # like this we copy
same_cart = amazon_cart1
same_cart[0] = 'banana'
new_cart[0] = 'gum'
print(amazon_cart1)
print(same_cart)
print(new_cart)

# matrix
# multi dimensional lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])
print(matrix[1][1])

# list methods

print(len(amazon_cart1))

new_list = ['apples', 'banana', 'strawberry']
print(new_list.append(100))
print(new_list)
new_list.insert(0, 'peppermint')
print(new_list)
new_list.remove('banana')
print(new_list)
new_list.extend([100, 1001])
print(new_list)

new_list.pop(0)  # removes by index
print(new_list)
new_list.pop()  # removes the last element, pop returns a value and we can assign it to a new data item1 = new_list.pop(1)
print(new_list)

letters = [
    'a', 'b', 'c', 'd', 'x', 'e'
]
print(letters)
print(letters.index('c'))  # to find the index, where it is located

# to look for smth in a list but we are not sure if it is there, we use a keyword

print('a' in letters)
print(1 in letters)
print('i' in 'hi my  name is Florin')
print(letters.count('d'))  # counts how many times the value occurs

letters.sort()  # sort the list
print(letters)  # we can also do a function sorted sorted(letters)
# if we run sorted in a print function, we will produce a new list, not modify the previous list

letters.reverse()
print(letters)

print(letters[::-1])  # reverse without the reverse method, creates a new list version

#  generate a list
print(list(range(1, 100)))
print(list(range(101)))  # get a list from 0 to 100

sentence = '        '
new_sentence = sentence.join(['hi', 'hello'])
print(new_sentence)

# list unpacking

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# assign a variable to each item

print(a)
print(b)
print(c)
print(other)
print(d)

# none, similar to null

weapons = None
print(weapons)


# dictionary

dictionary = {
    'a': 1,
    'b': 2
}  # a is the key and 1 is the value
print(dictionary['a'])
print(dictionary)

dictionary1 = {
    'a': [1, 2, 3, 4],
    'b': 'hello',
    'c': True,
}

# I can also have dictionary in the array

user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age' :20
}

print(user.get('age', 'nothing found')) # to check if we have age key and if there is any value without error

# another way to make a dictionary

user2 = dict(name='John')
print(user2)

# to look for an item in a dictionary

print('age' in user)
print('age' in user.keys())  # .keys() will check all the keys

# to grab the entire items

print(user.items())

# .clear() will empty up the dictionary
# .copy() will copy  up a dictionary user2 = user.copy()
# .pop() will return the value that has been removed from dict print(user.pop())

print(user.popitem()) # randomly removes something 4

# .update({'age' : 55}) : updates the value of the key in the dict

# Tuples

my_tuple = (1, 2, 3, 4, 5)
# tuple is immutable
print(my_tuple[1])
print(5 in my_tuple)
# the only difference is that is immutable
# difference between tuple and list: tells other programmers that this should not be change
# cannot sort or run reverse on a tuple but they are more preformat than a list

new_tuple = my_tuple[1:2]
print(new_tuple)
# tuple takes one by one

x,y,z, *other = (1,2,3,4,5)
print(x)
print(other)

print(my_tuple.count(5)) # how many 5's occur
print(my_tuple.index(5))
print(len(my_tuple))

# sets

my_set = {1, 2, 3, 4, 5, 5}
# set is an unordered collection of objects
print(my_set) # return the unique items

my_set.add(100)
my_set.add(2) # it will not be added because it exists already

print(my_set)

big_list = [1, 2, 3, 4, 5, 5]
# return a collection with unique items
print(set(big_list))

print(1 in my_set)
print(len(my_set))  # counts the unique elements
print(list(my_set))

new_set = my_set.copy()
print(new_set)

print(new_set.clear())


my_set = {1, 2, 3, 4, 5, }
your_set ={4, 5, 6, 7, 8, 9, 10}

# set operations: difference(), discard(), difference_update(), isdisjoint(), issubset(), issuperset(), union()





