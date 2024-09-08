

def add_numbers(number_string):
    # return 0 on the empty string
    if not number_string:
        return 0
    number_list = number_string.split(",")
    return sum([int(number) for number in number_list])



if __name__ == "__main__":
    input_string = input("Enter a string of numbers: ")
    print(add_numbers(input_string))
