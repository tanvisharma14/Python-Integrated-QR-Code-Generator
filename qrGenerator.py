# install pyqrcode
# install pypng

import pyqrcode

content = "This is my python QR Code Generator Project"

url = pyqrcode.create(content)
url.png("myQr.png", scale=5)

print("QR Code generated successfully")
