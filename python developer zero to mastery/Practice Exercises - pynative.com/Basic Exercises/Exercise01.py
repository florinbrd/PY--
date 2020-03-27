# Question 1: Accept two int values from the user and return their product.
# If the product is greater than 1000, then return their sum

def total(num1, num2):
    sum_total = num1 + num2
    if sum_total > 1000:
        return f'Your total sum is: {sum_total}'
    else:
        return 'value too small'


x = int(input('Enter your first number: '))
y = int(input('Enter your second number: '))

print(total(x,y))
