import qrcode

#Data to be encoded
data = 'https://leedscitycollege.ac.uk/'

#Encoding data using make() function
qr_img = qrcode.make(data)

#Saving as an image file
qr_img.save('WebQRCode.png')
