# Description: This is the main file for the string calculator
# The add_numbers function takes a string of numbers and returns the sum of the numbers

def add_numbers(number_string):
    # return 0 on the empty string
    if not number_string:
        return 0
    number_list = number_string.split(",")
    return sum([int(number) for number in number_list])





if __name__ == "__main__":
    # The main function takes user input and calls the add_numbers function
    input_string = str(input("Enter a string of numbers: "))
    print(add_numbers(input_string))
