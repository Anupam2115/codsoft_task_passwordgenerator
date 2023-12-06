# ANUPAM KUMAR VERMA MCA1st Year CodSoft Internship
import random
import string

# password Complexity define conditions
def generate_password(length, complexity):
    if complexity == "weak":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# Password Creation
def main():
    print("Welcome to the Password Generator!(Made by Anupam Kumar Verma)")

    length = int(input("Enter the length of the password which you want for your security: "))
    complexity = input("Enter the level of your password like select any one from this:-[weak, medium, strong]: ")

    password = generate_password(length, complexity)

    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()