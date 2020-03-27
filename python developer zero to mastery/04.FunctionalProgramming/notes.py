#  Pure functions
# given the same input, will return the same output
#  should not produce any side effects
''
def multiply2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return  print(new_list)

multiply2([1,2,3])  # this is a function as it returns the same output
# also it does not interact with the outside world
# if new list was defined outside of the function, it would have produced side effects

