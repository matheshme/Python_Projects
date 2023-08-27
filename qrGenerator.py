import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,box_size=10,border=5,error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('https://www.name.com') # You have to give your own url link
qr.make(fit=True)
img=qr.make_image()
img.save('test.png')
img.show()