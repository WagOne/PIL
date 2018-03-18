from PIL import Image, ImageDraw, ImageFont,ImageFilter
img = Image.open("")#link to file
blurred_image = img.filter(ImageFilter.GaussianBlur(radius=20))
d = ImageDraw.Draw(blurred_image)
fnt = ImageFont.truetype('VCR Font + Cyrillic.ttf', 140)
d.text((200,500), "Hello \nworld", font=fnt, fill=(255, 255, 0))
blurred_image.show()
