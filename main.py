import random
import secrets
import string

#random
def generate_password(pwd_length=12):
    # Define the alphabet
    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Generate a password
    pwd = ''.join(random.choice(alphabet) for i in range(pwd_length))

    # Customize the password based on constraints
    if not any(char.isdigit() for char in pwd):
        pwd = generate_password()
    if not any(char.isupper() for char in pwd):
        pwd = generate_password()
    if not any(char.islower() for char in pwd):
        pwd = generate_password()
    if not any(char in string.punctuation for char in pwd):
        pwd = generate_password()

    return pwd

# Generate a password
password = generate_password()

print("random : " + password)

#secret
def generate_password(pwd_length=12):
    # Define the alphabet
    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Generate a password
    pwd = ''.join(secrets.choice(alphabet) for i in range(pwd_length))

    # Customize the password based on constraints
    if not any(char.isdigit() for char in pwd):
        pwd = generate_password()
    if not any(char.isupper() for char in pwd):
        pwd = generate_password()
    if not any(char.islower() for char in pwd):
        pwd = generate_password()
    if not any(char in string.punctuation for char in pwd):
        pwd = generate_password()

    return pwd

# Generate a password
password = generate_password()
print("secret : " + password)



