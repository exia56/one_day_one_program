import Image, ImageDraw, ImageFont
import random

img=Image.open("pic.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype(font = "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",size = 24)
random.seed()
rand = str((int)(random.random() * 10))
draw.text((20,20),str(rand), font=font, fill=(0,255,0,255))
img.save(rand+".jpg")
