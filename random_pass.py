import random
import string

def generate_password(length):
    # Define 
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate
    password = "".join(random.choice(all_chars) for i in range(length))
    
    return password

# Test 
password = generate_password(8)
print(password)
