# Description: This is the main file for the string calculator
# The add_numbers function takes a string of numbers and returns the sum of the numbers

def add_numbers(number_string):
    # return 0 on the empty string
    if not number_string:
        return 0
    string_with_number = replace_custom_delimiter_with_comma(number_string)
    number_list = string_with_number.split(",")
    positive_number_list = []
    negative_number_list = []
    for number in number_list:
        if int(number) < 0:
            negative_number_list.append(number)
        else:
            positive_number_list.append(int(number))
    if negative_number_list:
        raise ValueError(f"negative numbers not allowed: {', '.join(negative_number_list)}")
    return sum(positive_number_list)


def replace_custom_delimiter_with_comma(string):
    # This function replaces the custom delimiter with a comma and handles the new line character
    delimiter = "\n"
    if string.startswith("//"):
        splitup_strings = string[2:].split("\n")
        delimiter = splitup_strings[0]
        string = delimiter.join(splitup_strings[1:])
    new_string = string.replace(delimiter, ',')
    return new_string


if __name__ == "__main__":
    # The main function takes user input and calls the add_numbers function
    input_string = str(input("Enter a string of numbers: "))
    try:
        input_string = input_string.replace("\\n", "\n")
        print(add_numbers(input_string))
    except ValueError as exception:
        print(exception)