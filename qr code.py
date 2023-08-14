import qrcode

data = "https://www.youtube.com/channel/your_channel_id"

img = qrcode.make(data)

assert isinstance(img, object)
img.save("white_world_of_music_qr_code.png")