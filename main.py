#Joel Samuel
#10/24

def menu():
    print("Menu ")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):
    new = ""
    for i in password:
        a = int(i) - 3
        b = str(a)
        new += b
    return new

def decode(password):
    # Enter code here

def main():
    password = ""
    encoded_password = ""

    while True:
        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!")
            print()


        elif menu_option == 2:
             # add decoder here
             pass

        elif menu_option == 3:
                break

if __name__ == '__main__':
    main()