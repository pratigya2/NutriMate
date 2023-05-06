import qrcode
import os
from django.conf import settings
def generate(name,link,path):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(link)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black",back_color = "white")
    img_path = os.path.join(settings.MEDIA_ROOT, path)
    img.save(path)
    return path