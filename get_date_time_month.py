"""
Python Task-5
    5) Use a lambda function to extract the year, month, and day from a datetime object.
"""

# Importing datetime from datetime module
from datetime import datetime

def main():

    # Getting today's date from datetime object
    curr_date = datetime.today()
    print("Current date and time: ", curr_date)

    # Using Lambda function to extract year, month and day from datetime object
    extract = lambda date: (date.year, date.month, date.day)
    year, month, day = extract(curr_date)
    print("After extraction of year, month, day - ", end =" ")
    print("Year: {}, Month: {}, Day: {}".format(year, month, day))

if __name__ == "__main__":
    main()