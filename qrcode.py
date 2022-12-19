import pyqrcode
from pyqrcode import QRCode

# String which represent the QR code
s = "https://www.youtube.com/playlist?list=PLu0W_9lII9agK8pojo23OHiNz3Jm6VQCH"

# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.svg("myyoutube.svg", scale=8)