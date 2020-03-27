# Question 9: Reverse a given number and return true if it is the same as the original number

def reversenumber(number):
    original_number = number
    reversed1 = 0
    while number > 0:
        reversed1 = reversed1 * 10 + number % 10
        number = number // 10
    if original_number == reversed1:
        return True
    else:
        return False


print(reversenumber(23))
