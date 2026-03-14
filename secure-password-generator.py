import random
import string


def is_digit(num):
    return num.isdigit()


def password_generator(
    quantity,
    length,
    add_digits,
    add_uppercase,
    add_lowercase,
    add_punctuation,
    no_amb_chars,
):

    digits = string.digits
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    punctuation = "!#$%&*+-=?@^_"

    result = []
    cur_password = []
    chosen_sets = []
    all_chars = []

    if int(add_digits) == 1:
        chosen_sets.append(digits)

    if int(add_uppercase) == 1:
        chosen_sets.append(uppercase_letters)

    if int(add_lowercase) == 1:
        chosen_sets.append(lowercase_letters)

    if int(add_punctuation) == 1:
        chosen_sets.append(punctuation)

    if int(no_amb_chars) == 1:
        for i in range(len(chosen_sets)):
            for j in "il1Lo0O":
                chosen_sets[i] = chosen_sets[i].replace(j, "")

    for char in chosen_sets:
        all_chars.extend(char)

    for _ in range(int(quantity)):

        for cur_set in chosen_sets:
            cur_password.append(random.choice(cur_set))

        for _ in range(int(length) - len(cur_password)):
            cur_password.append(random.choice(all_chars))

        random.shuffle(cur_password)
        result.append("".join(cur_password))
        cur_password = []

    return result


def play():

    while True:

        quantity = input("Number of passwords to generate: ")
        while not is_digit(quantity):
            quantity = input("Please enter a number: ")

        length = input("Length of each password: ")
        while not is_digit(length):
            length = input("Please enter a number: ")

        add_digits = input("Include digits 0123456789? Yes: 1, No: 0 ")
        while not is_digit(add_digits):
            add_digits = input("Please enter a number: ")

        add_uppercase = input(
            "Include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ? Yes: 1, No: 0 "
        )
        while not is_digit(add_uppercase):
            add_uppercase = input("Please enter a number: ")

        add_lowercase = input(
            "Include lowercase letters abcdefghijklmnopqrstuvwxyz? Yes: 1, No: 0 "
        )
        while not is_digit(add_lowercase):
            add_lowercase = input("Please enter a number: ")

        add_punctuation = input("Include symbols !#$%&*+-=?@^_? Yes: 1, No: 0 ")
        while not is_digit(add_punctuation):
            add_punctuation = input("Please enter a number: ")

        no_amb_chars = input("Exclude ambiguous characters il1Lo0O? Yes: 1, No: 0 ")
        while not is_digit(no_amb_chars):
            no_amb_chars = input("Please enter a number: ")

        print(
            f"Your {quantity} password(s):",
            *password_generator(
                quantity,
                length,
                add_digits,
                add_uppercase,
                add_lowercase,
                add_punctuation,
                no_amb_chars,
            ),
            sep="\n",
        )

        more = input("Do you want to generate password again? Yes: 1, No: 0 ")
        while not is_digit(more):
            more = input("Please enter a number: ")
        if int(more) != 1:
            break


print("Hello! I'm secure password generator. Let's start!")
play()
