

calculation_to_units = 24
name_of_units = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}\n"


def validate_input():
    try:

        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered 0, please enter a positive number of days!\n")
        else:
            print("You entered a negative number, no conversion!\n")
    except ValueError:
        print("Your input is not a whole number, you trying to crash my program?\n")


user_input = ""
while user_input != "exit":
    user_input = input(
        "Hey User! Enter a number of days and i will convert it to hours:\n")
    validate_input()
