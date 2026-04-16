"""
Python Task-5
    3) Write a list comprehension that creates a new list of squares of even numbers from a
    given list, using a lambda function to check for even numbers.
"""

# Define given list globally
given_list = [102, 25, 8, 1, 17, 11, 2, 35, 16, 22, 121, 90, 15, 130, 3]

def main():

    # Lambda function to check for even num
    check_even = lambda num: num % 2 == 0

    # Using list comprehension to find squares of even nums in list
    sq_even_nums_list = [num**2 for num in given_list if check_even(num)]
    
    print("Given list: ", given_list)
    print("Even numbers in the given list: ", [num for num in given_list if check_even(num)])
    print("List of squares of even numbers from given list: ", sq_even_nums_list)

if __name__ == "__main__":
    main()
