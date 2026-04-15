"""
Python Task-5
    4) Write a lambda function to check if a given string is a number.
"""

def main():

    # Define string_to_check and get user input for the value
    string_to_check = input("Enter a string: ")

    # Using lambda function to check if a string is number
    check_str = lambda string: string.isnumeric()

    # Check if given string is a number
    if check_str(string_to_check):
        print("Given string \"{}\" is a number".format(string_to_check))
    else:
        print("Given string \"{}\" is not a number".format(string_to_check))

if __name__ == "__main__":
    main()
