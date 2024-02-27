import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Strong Password Generator!")
    print("-----------------------------------------")
    print("This program will generate strong and secure passwords for you.")

    while True:
        try:
            num_passwords = int(input("\nEnter the number of passwords you want to generate: "))
            length = int(input("Enter the length of each password: "))
            if num_passwords <= 0 or length <= 0:
                raise ValueError("Number of passwords and length must be positive integers.")
            break
        except ValueError as e:
            print("Invalid input. Please enter positive integers for number of passwords and length.")

    print("\nGenerated Passwords:")
    for i in range(num_passwords):
        password = generate_password(length)
        print(f"Password {i+1}: {password}")

    print("\nThank you for using the Strong Password Generator!")

if __name__ == "__main__":
    main()
