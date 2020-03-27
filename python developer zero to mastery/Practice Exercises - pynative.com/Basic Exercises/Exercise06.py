# Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

def iterate_by_5(list):
    for item in range(len(list)):
        if list[item] % 5 == 0:
            print(list[item])

work_list = [1, 2, 3, 5, 10, 20]

iterate_by_5(work_list)
