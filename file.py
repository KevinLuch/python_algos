# *****************************************************************
# Python code that adds two numbers
num1 = 69
num2 = 5
# Adding two numbers
sum = num1 + num2
# Printing values
print("Sum of {0} and {1} is {2}" .format(num1, num2, sum))
# *****************************************************************
# Python code that finds the maximun of two numbers once given
def maximum(a,b):
    # if a is greater than or equal to b return a
    if a >= b:
        return a
    # if a is not greater than or equal to b return b
    else:
        return b
# Printing values
print(maximum(2,4))
# *****************************************************************
# Python code to find the factorial of a given number
def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n ==1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact 

num = 10
print("Factorial of", num, "is", factorial(num))
# *****************************************************************
# Python code that calculates simple interest
def simple_interest(p, t, r):
    print('The principle is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r)/100

    print('The Simple Interest is', si)
    return si

simple_interest(8, 6, 8)
# *****************************************************************
# Python code that finds compound interest for a given value
def compound_interest(principle, rate, time):
    # calcuates compound interest 
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle 
    print("Compound interest is", CI)

compound_interest(10000, 10.25, 5)