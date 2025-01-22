from stegano import lsb

# Encode a secret message into an image
def encode_message(input_image, output_image, secret_message):
    secret = lsb.hide(input_image, secret_message)
    secret.save(output_image)
    print(f"Message encoded into {output_image}.")

# Example usage
input_image = "Ferrari.jpeg"  # Replace with your image file
output_image = "encoded_image.png"
secret_message = "This is a hidden message!"

encode_message(input_image, output_image, secret_message)
