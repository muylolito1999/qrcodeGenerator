import qrcode
from PIL import Image

# taking image which user wants 
# in the QR code center
Logo_link = '/home/lollo/qrcodeGenerator/logoCorteGalluzzi.jpeg'

logo = Image.open(Logo_link)

# taking base width
basewidth = 400

# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

# taking url or text
url = 'https://www.google.it/maps/place/Trattoria+La+Corte+Galluzzi/@44.4920106,11.3420926,15z/data=!4m8!3m7!1s0x477fd4955eb82fed:0xdd34f893953d835f!8m2!3d44.4920106!4d11.3420926!9m1!1b1!16s%2Fg%2F1tzvvd9h?entry=ttu&g_ep=EgoyMDI0MDgyMS4wIKXMDSoASAFQAw%3D%3D'

# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking color name from user
QRcolor = 'Black'

# adding color to QR code
QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
       (QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save('QRcorte.png')

print('QR code generated!')
