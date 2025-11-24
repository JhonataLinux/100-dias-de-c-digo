import wifi_qrcode_generator.generator
from PIL import Image
ssid = "WIFI_5G_23D8E8"
password = "12345678"
security = "WPA"

from wifi_qrcode_generator.generator import wifi_qrcode
qr = wifi_qrcode(ssid, False, security, password)

qr.make_image().save("wifi_qr.png")
Image.open("wifi_qr.png")
