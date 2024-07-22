import qrcode
from qrcode.constants import ERROR_CORRECT_L

url = "http://equipekb.shop:8000/app/appbanco"
qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save("equipekb.png")
print("QR code generated successfully!")
