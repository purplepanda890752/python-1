import random
import string

def generate_password(length=12):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    
    all_chars = lower + upper + digits
    password = random.sample(all_chars, length)
    random.shuffle(password)  # Shuffle to add randomness
    
    return "".join(password)

# Example usage
password_length = int(input("Enter password length: "))
print("Generated Password:", generate_password(password_length))