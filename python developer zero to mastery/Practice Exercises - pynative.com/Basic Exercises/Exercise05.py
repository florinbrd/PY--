# Question 5: Given a list of ints, return True if first and last number of a list is same

def list_operation(list):
    firstNumber = list[0]
    lastNumber = list[-1]
    if firstNumber == lastNumber:
        return True
    else:
        return False

work_list1 = [10, 20, 30, 40, 10]
work_list2 = [2, 5, 7, 1]

print(list_operation(work_list1))
print(list_operation(work_list2))
