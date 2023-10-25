#Joel Samuel
#10/24

#CM: made some changes to encode - it is supposed to add 3
def encode(password):
    new = ""
    for i in password:
        a = int(i) + 3 # CM: made a change here
        b = str(a)
        new += b
    return new

def decode(password):
    original = ""
    for i in password:
        a = int(i) - 3
        b = str(a)
        original += b
    return original

# Cahlie Menton
# 10/25
# Added my own decoder and main functions below
# As well as a print menu function

def print_menu():
    print("Menu ")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def decoder(password):
    password_nums = list(str(password))
    decoded_password_list = []
    decoded_password = ""
    for num in password_nums:
        decoded_password_list.append(int(num) - 3)
    for item in decoded_password_list:
        decoded_password += str(item)
    return decoded_password

def main():
    password = ""
    encoded_password = ""

    while True:
        menu_option = int(input("Please enter an option: "))


        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()


        elif menu_option == 2:
            decoded_password = decoder(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            print()

        elif menu_option == 3:
            break


if __name__ == '__main__':
    main()
