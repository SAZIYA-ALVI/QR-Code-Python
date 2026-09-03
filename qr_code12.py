
import qrcode
from PIL import Image


qr = qrcode.QRCode(
    version=1,error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,border=4,)

qr.add_data("https://www.youtube.com/@Saziya2004")
qr.make(fit=True)

img =qr.make_image(fill_color="green",back_color="white")
img.save("saziya_yt.png")