"""
Python Task-5
    1) Given a list of dictionaries, each representing a person with 'name' and 'age' keys,
    use lambda functions to filter out people under 18 and then map the remaining people's
    names to a new list.
"""

# Define given list of dictionaries globally
list_of_name_age_dict =[
                        {'name':'Kumar', 'age': 5}, {'name':'Yamini', 'age': 28},
                        {'name':'Alex', 'age': 30}, {'name':'Clara', 'age': 68},
                        {'name':'Isabel', 'age': 35}, {'name':'Henry', 'age': 18},
                        {'name':'Karthik', 'age': 2}, {'name':'Ivan', 'age': 17},
                        {'name':'Ayan', 'age': 15}, {'name':'Shobha', 'age': 16},
                        {'name':'Kumari', 'age': 82}, {'name':'Maria', 'age': 98},
                        {'name':'Frederick', 'age': 21}, {'name':'Mia', 'age': 24},
                        {'name':'Amy', 'age': 42}, {'name':'Naren', 'age': 53},
                        {'name':'Max', 'age': 77}, {'name':'Helen', 'age': 61},
                        {'name':'Linda', 'age': 12}, {'name':'Melvin', 'age': 11},
                        {'name':'Derek', 'age': 2}, {'name':'Raven', 'age': 1}
                        ]

def main():

    print("The given list of dictionaries representing a person with 'name' and 'age' keys: {}".format(list_of_name_age_dict))

    # Filtering persons with age less than 18 => minors
    minors_list = list(filter(lambda p: p['age'] < 18, list_of_name_age_dict))

    # Mapping persons name for minors
    minors_name_list = list(map(lambda p: p['name'], minors_list))
    print("Person names with age less than 18: ")
    for name in minors_name_list:
        print("\t",name)

    # Filtering persons with age >= 18 => adults
    adults_list = list(filter(lambda p: p['age'] >= 18, list_of_name_age_dict))

    # Mapping persons name for adults
    adults_name_list = list(map(lambda p: p['name'], adults_list))
    print("\nPerson names with age greater than or equal to 18: ")
    for name in adults_name_list:
        print("\t",name)

if __name__ == '__main__':
    main()
