from stegano import lsb

# Encode a secret message into an image
def encode_message(input_image, output_image, secret_message):
    secret = lsb.hide(input_image, secret_message)
    secret.save(output_image)
    print(f"Message encoded into {output_image}.")

# Example usage
input_image = input("Enter the input image filename: ")
secret_message = input("Enter the secret message: ")
output_image = input("Enter the output image filename: ")
encode_message(input_image, output_image, secret_message)