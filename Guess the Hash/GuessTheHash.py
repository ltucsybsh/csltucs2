import hashlib

# Function to generate a hash
def generate_hash(input_text):
    hash_object = hashlib.md5(input_text.encode())  # Change to hashlib.sha256() for SHA256
    return hash_object.hexdigest()

# Read the target word from a file and generate its hash
def get_target_hash(file_path):
    try:
        with open(file_path, 'r') as file:
            target_word = file.read().strip()  # Remove any extra whitespace or newline characters
        return generate_hash(target_word)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

# Path to the file containing the target word
target_file = 'target_word.txt'

# Generate the target hash
target_hash = get_target_hash(target_file)

if target_hash is None:
    print("Unable to proceed without a valid target hash.")
else:
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