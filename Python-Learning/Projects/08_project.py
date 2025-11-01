# QR Code Generator

import qrcode

data=input("Enter the input to make a QR Code:")

file_name=input("Enter the file name to save:")+ ".png"

qr=qrcode.QRCode()
qr.add_data(data)
qr.make(fit=True)

img=qr.make_image()
img.save(file_name)

print(f"QR code generated and saved as {file_name}!")
