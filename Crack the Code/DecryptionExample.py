def caesar_cipher(text, shift):
    result = ""
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Keep non-alphabetic characters as is
            result += char
    return result

# Encrypted message
encrypted_message = "Dwwdfk wkh frgh"
print("The encrypted message is:", encrypted_message)
# Test the cipher function with a given shift
shift = 3  # Modify this for experimentation
decrypted_message = caesar_cipher(encrypted_message, -shift)
print("Decrypted message with shift", shift, "is:", decrypted_message)