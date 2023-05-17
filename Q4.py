# This is a dodgy calculator

# function to multiply or divide
def times_or_divide(operation, num_one, num_two):
    # choose operation
    if operation == "*":
        return num_one * num_two
    elif operation == "/":
        return num_one / num_two
    else:
        raise ValueError("Invalid operation")
    
# function to add or subtract
def add_or_subtract(operation, num_one, num_two):
    # choose operation
    if operation == "+":
        return num_one + num_two
    elif operation == "-":
        return num_one - num_two
    else:
        raise ValueError("Invalid operation")
    
def get_number():
    # This loops until the user enters a valid number
    while True:
        try:
            user_input = input("Enter a number > ")
            return float(user_input)
        except ValueError:
            print("Invalid input")


if __name__ == "__main__":
    # get the first number
    print('Welcome to basic arithmetic calcs ...')
    while True:
        # get the first number
        num_one = get_number()
        # get the operation
        while True:
            operation = input("Enter an op ['+', '-', '*', '/'] >")
            if operation in ['+', '-', '*', '/']:
                break
            else:
                print("Invalid input")

        # get the second number
        num_two = get_number()

        # choose operation
        if operation in ["*", "/"]:
            print(times_or_divide(operation, num_one, num_two))
        else:
            print(add_or_subtract(operation, num_one, num_two))

        print("Do you want to calculate again? (y/n)")
        if input() != "y":
            print("Goodbye")
            break