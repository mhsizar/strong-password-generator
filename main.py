import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

repeat=True
while repeat:

    int_value=True
    while int_value:
        try:
            nr_letters = int(input("How many letters would you like in your password?\n"))
            int_value=False
        except:
            print("Wrong Command! Please enter a number!")
            int_value=True
    int_value=True
    while int_value:
        try:
            nr_symbols = int(input(f"How many symbols would you like?\n"))
            int_value=False
        except:
            print("Wrong Command! Please enter a number!")
            int_value=True
    int_value=True
    while int_value:
        try:
            nr_numbers = int(input(f"How many numbers would you like?\n"))
            int_value=False
        except:
            print("Wrong Command! Please enter a number!")
            int_value=True
    
    pass_letters = random.choices(letters, k=nr_letters)
    pass_symbols = random.choices(symbols, k=nr_symbols)
    pass_numbers = random.choices(numbers, k=nr_numbers)

    password_list = []
    
    for l in pass_letters:
        password_list += l
    for n in pass_numbers:
        password_list += n
    for s in pass_symbols:
        password_list += s
    
    random.shuffle(password_list)
    password = ""
    for random_pass in password_list:
        password += random_pass
    print(f'Your password is: {password}')

    run_again = input(
        "\nDo you want to generate another password? Reply with 'yes' or 'no': \n"
    ).lower()[0]
    while run_again != "y" and run_again != "n":
        print("Wrong input! Please reply with 'yes' or 'no'")
        run_again = input(
            "\nDo you want to generate another password? Reply with 'yes' or 'no': \n"
        ).lower()[0]
    if run_again == "y":
        repeat = True
    elif run_again == "n":
        print("Goodbye!")
        repeat = False
