"""
Python Task-5
    2) Given a list of numbers, use the reduce function and a lambda expression to calculate
    the product of all the numbers in the list.
"""

# Importing reduce function
from functools import reduce

# Define list of numbers globally
given_list = [90, 11, 32, 1, 5, 23, -8]

def main():

    # Using reduce function and a lambda expression to calculate product of all nums in the list
    prod_of_all_num = reduce(lambda x, y: x*y, given_list)

    print("Given list: ", given_list)
    print("Product of all numbers in the list: ", prod_of_all_num)

if __name__ == "__main__":
    main()