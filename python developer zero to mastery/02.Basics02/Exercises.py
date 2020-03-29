# create a def highest even(list):

def highesteven(list):
    evens = []
    for item in list:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)

print(highesteven([1,2,3,4,5,6]))
