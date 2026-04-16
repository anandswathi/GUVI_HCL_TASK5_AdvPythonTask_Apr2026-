"""
Python Task-5
    6) Create a lambda function to generate a Fibonacci series up to n terms.
"""

# Importing reduce function
from functools import reduce

def fibonacci_series(n):
    """
    Function to generate a Fibonacci series up to n terms.
    Input: param n(Integer) the number of terms to generate.
    Return: Fibonacci series up to n terms.
    """

    # initial list
    init_list = [0,1]

    # Lambda function to generate Fibonacci series up to n terms
    fib_series = lambda x: reduce(lambda series,_ : series + [series[-1] + series[-2]], range(2,n), init_list)

    return fib_series(n) # returns fib_series upto n terms


def main():

    # Get the no. of terms value from user
    n = int(input("Enter value for n: "))

    # Function call for fibonacci_series
    fib_series = fibonacci_series(n)
    print("The Fibonacci series up to {} terms: {}".format(n,fib_series))

if __name__ == "__main__":
    main()
