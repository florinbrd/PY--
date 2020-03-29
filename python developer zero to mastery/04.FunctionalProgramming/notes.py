#  Pure functions
# given the same input, will return the same output
#  should not produce any side effects


def multiply2(li):
    new_list = []
    for item in li:
        new_list.append(item * 2)
    return print(new_list)


multiply2([1, 2, 3])  # this is a function as it returns the same output
# also it does not interact with the outside world
# if new list was defined outside of the function, it would have produced side effects


#map(), filter(), zip(), reduce()

#map allows us to simply the code
#map(action, data)
#some data is given and the action is taken by the function

def multiply2_map(item):
    return item*2

print(list(map(multiply2_map, [1,2,3])))
# it automatically runs the function without the rest of the code

my_list = [1,2,3]
print(list(map(multiply2_map, my_list)))
print(my_list) # this has not changed, principle of functions that the outside world remains intact

# filter helps to filter the results

def check_odd(item):
    return item % 2 != 0

print(list(filter(check_odd, my_list)))
print(my_list)

your_list = [10, 20, 30]

print(list(zip(my_list, your_list)))
print(your_list)
# in this situation we have tuples with values from both lists
# it would create the same if my_list and your_list would be tuples

their_list = [4,5,6]
print(list(zip(my_list, your_list, their_list)))

# reduce does not come as a built in function
# we need to import it

from functools import reduce

def accumulator(acc, item):
    return acc+item

print(reduce(accumulator, my_list, 0))
# reduce accumulated the values, 0 it was the initial value assigned to the accumulator
# later the rest of the values from my_list has been accumulated 1+ 2 + 3 
