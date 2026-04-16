# Importing all files required for Python Task-5
import lambda_and_map_to_filter
import find_prod_of_all_num_in_list
import find_square_of_even_nums_in_list
import check_if_given_string_is_num
import get_date_time_month
import fibonacci_series_using_lambda

# Main file containing main function calls for all required modules
def main():
    print("--------------------------------------------------------------------")
    print("                                TASK 5 - Q1                         ")
    print("--------------------------------------------------------------------")
    lambda_and_map_to_filter.main() # Calling main from lambda_and_map_to_filter module
    print("-----------------------------xxxxxxxxxx-----------------------------\n\n")

    print("--------------------------------------------------------------------")
    print("                                TASK 5 - Q2                         ")
    print("--------------------------------------------------------------------")
    find_prod_of_all_num_in_list.main() # Calling main from find_prod_of_all_num_in_list module
    print("-----------------------------xxxxxxxxxx-----------------------------\n")

    print("--------------------------------------------------------------------")
    print("                                TASK 5 - Q3                         ")
    print("--------------------------------------------------------------------")
    find_square_of_even_nums_in_list.main() # Calling main from find_square_of_even_nums_in_list module
    print("-----------------------------xxxxxxxxxx-----------------------------\n")

    print("--------------------------------------------------------------------")
    print("                                TASK 5 - Q4                        ")
    print("--------------------------------------------------------------------")
    check_if_given_string_is_num.main() # Calling main from check_if_given_string_is_num module
    print("-----------------------------xxxxxxxxxx-----------------------------\n")

    print("--------------------------------------------------------------------")
    print("                                TASK 5 - Q5                         ")
    print("--------------------------------------------------------------------")
    get_date_time_month.main() # Calling main from get_date_time_month module
    print("-----------------------------xxxxxxxxxx-----------------------------\n")

    print("--------------------------------------------------------------------")
    print("                                TASK 5 - Q6                         ")
    print("--------------------------------------------------------------------")
    fibonacci_series_using_lambda.main() # Calling main from fibonacci_series_using_lambda module
    print("-----------------------------xxxxxxxxxx-----------------------------\n")

if __name__ == "__main__":
    main()