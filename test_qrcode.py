import qrcode
from qrcode.constants import ERROR_CORRECT_L

url = "http://equipeguilhermeleal.shop:8688/app/appbanco"
qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save("equipeguilhermelelal.png")
print("QR code generated successfully!")
