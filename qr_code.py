import qrcode

website_link = "https://youtu.be/nhkNYjljbMs?si=luxtn3nd1BwPXgpz"

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_colour = 'black', back_color = 'white')
img.save('imgs/youtube_qr.png')