# Question 10: Given a two list of ints create a third list such that should contain only odd numbers from the first list and even numbers from the second list

def odd_list(list1, list2):
    list3 = []

    for item1 in list1:
        if item1 % 2 == 0:
            list3.append(item1)

    for item2 in list2:
        if item2 % 2 == 0:
            list3.append(item2)

    return list3


work_list1 = [1, 2, 3, 4, 5, 6, 7, 8]
work_list2 = [10, 11, 12, 13, 14, 15]

print(odd_list(work_list1, work_list2))
