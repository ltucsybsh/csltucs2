# pip install qrcode[pil]

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import HorizontalGradiantColorMask
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer

# Text to encode in the QR code
text = """
YashB eVisit card
Dr Yashar Baradaranshokouhi
Follow me on:
LinkedIn: https://www.linkedin.com/in/ybshokouhi/
X: https://x.com/_YashB_
Email: yashb@leedstrinity.ac.uk
"""

# Create the QR code
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box
    border=4,  # Border width
)
qr.add_data(text)
qr.make(fit=True)

# Create a styled QR code image
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=GappedSquareModuleDrawer(),
    color_mask=HorizontalGradiantColorMask(
        left_color=(0, 0, 255),  # Blue
        right_color=(255, 0, 0)  # Red
    )
)

# Save the QR code
img.save("Your_Contact_Me_QRCard.png")

print("Your_Contact_Me_QRCard.png")
