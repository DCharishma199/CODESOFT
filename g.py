import random
import string

def generate_password(length):
    # Define characters to use for generating the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choices() for Python 3.6+
    password = ''.join(random.choices(characters, k=length))

    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
            return
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
