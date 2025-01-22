import hashlib

# Function to generate a hash
def generate_hash(input_text):
    hash_object = hashlib.md5(input_text.encode())  # Change to hashlib.sha256() for SHA256
    return hash_object.hexdigest()

# Predefined hash for students to guess (hash of "hello")
target_hash = "5d41402abc4b2a76b9719d911017c592"

print("Welcome to 'Guess the Hash'!")
print("Your goal is to find the original text for this hash:")
print(target_hash)

while True:
    user_input = input("Enter your guess: ")
    hashed_input = generate_hash(user_input)

    if hashed_input == target_hash:
        print(f"Correct! The original text is '{user_input}'.")
        break
    else:
        print("Incorrect. Try again!")