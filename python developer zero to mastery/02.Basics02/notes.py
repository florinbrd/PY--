# ---> conditional logic
# if, elif, else
# operators: and, or, not

is_old = False
is_young = True

if is_old:
    print('you are old')
elif is_young:
    print('you are young')
else:
    print('you are not young or old')

if is_old or is_young:
    print('you are something')

if not is_old:
    print('you are not old')

# ---> Truthy and Falsy
# python can convert numerals or strings into booleans

is_old2 = bool('hello')
is_young = bool(5)
print(bool('hello'))
print(bool(5))  # it evaluates them into truth
# empty string or 0 is Falsy

print(bool(''))
print(bool(0))
print(bool(None))

# ---> Ternary operators
# condition_if_true if condition else condition_if_false

is_friend = True
can_message = 'message allowed' if is_friend else 'not allowed to message '
print(can_message)

# --> Logical operators
#  >, <, == , >= ,  =<, !=
# and or not
print(5 == 5)
print(not (True))

# --> Small exercise

is_magician = False
is_expert = True

# check if magician AND expert: 'you are a master magician'
# check if magician but not expert: you are getting there
# check if you are not a magician : 'you need magic powers'

if is_magician and is_expert:
    print('You are a master magician')
elif is_magician and not is_expert:
    print('You are getting there')
elif not is_magician:
    print('You need magic powers')

# ---> is vs ==

print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])  # it will check the values

print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])  # all of them will result as False because it will check the location in the memory
# so therefore it cannot be the same value check like in the case of ==

# ---> For loops

for item in "hello":
    print(item)  # will print each char element

for item in [1, 2, 3, 4, 5]:
    print(item)  # same like in char

for item in (1, 2, 3, 4, 5):
    print(item)  # same like in char

for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x)

# iterable - can be a list, dictionary or tuple, set, string
# go one by one to check each item in the collection

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

user2 = {
    'name': 'Golum',
    'age ': 22,
    'can_swim': False
}

for item in user:
    print(item)  # will print just the keys

for item in user2.items():
    print(item)  # will print the keys and the values

for item in user.values():
    print(item)  # will print just the values

for key, value in user.items():
    print(key, value)

# counter

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for item in my_list:
    sum += item
print(sum)

# range()

for number in range(0, 10):
    print(number)

for number in range(0, 10, 2):
    print(number)

for _ in range(2):
    print(list(range(10)))

# enumerate

for i, char in enumerate('hello'):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is : {i}')

# while loops

i = 0
while i < 50:
    print(i)
    i += 1
else:
    print('all the work is done')

while i < 50:
    print(i)
    break

# while True:
#   input('say something: ')
#  break   # breaks out of the loop, without it will go on infinite

# while True:
#  response = input('tell me something')
# if(response == 'bye'):
#   break

# besides break we can also continue which will go back to the loop
# it will not break/ terminate the code lines
# there is another one called pass which would not a lot of effects into the code

# check duplicates in a list

some_list = ['a', 'a', 'b', 'c', 'd', 'd', 'e', 'f']

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)


# functions functions functions

def say_hello():
    print('This is your turn to be awesome ')


say_hello()


# we can also give them parameters

def say_hi(name):
    print(name)


say_hi('mama')
# 'mama' is a positional argument and in case of more parameters, position matters
# arguments will be called the values given to the functions
# parameters we use when we define, arguments when we call

# keyword arguments / order does not matters
say_hi(name='Florin')


# return return return

def sum(num1, num2):
    total = num1 + num2
    return total


print(sum(1, 2))


def sum2(num1, num2):
    def second_function(num1, num2):
        return num1 + num2

    return second_function(num1, num2)


total = sum2(10, 20)
print(total)


# DOCSTRINGS DOCSTRINGS DOCSTRINGS

def test(a):
    """
    :param a: defined as a string
    :return: returns a string
    """
    print(a)


# arguments and key word arguments args / kwargs *args **kwargs

def superfunc(*args):  # by adding a star we can give as many as we want
    print(args)  # we get a tuple with it


superfunc(1, 2, 3, 4, 5)


def funk(**kwargs):
    print(kwargs)


# with kwargs we get a dictionary

print(funk(num1=5, num2=5))

# SCOPE

# scope means what variables do I have access to
# print(name), clicking run will give an error because name does not exist
# this happens because of scope/ what do I have access to?
