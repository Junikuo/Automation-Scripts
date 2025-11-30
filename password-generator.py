import random
import string

print("======= Welcome =======")

password_length = int(input("How long should your password be? "))

characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for _ in range(password_length))

print("\nYour password is:", password)
