from stegano import lsb

# Decode the hidden message from an image
def decode_message(encoded_image):
    secret_message = lsb.reveal(encoded_image)
    print(f"Hidden message: {secret_message}")

# Example usage
encoded_image = "encoded_image.png"  # Replace with your encoded image file
decode_message(encoded_image)
