from PIL import Image
import random

background = Image.open("background1.png")
foreground = Image.open("apple.png")

def test(im):
	return im

width, height = background.size
x,y = int(width/2.1),height//3
k=0
while k<1000:
	for i in range(10):
		background = Image.open("background1.png")
		background.paste(foreground, (x,y- (4*i)), foreground)
		background.save(f'images/image{str(k).zfill(3)}.png')
		k+=1
	for j in range(10,0,-2):
		background = Image.open("background1.png")
		background.paste(foreground, (x,y- (2*j)), foreground)
		background.save(f'images/image{str(k).zfill(3)}.png')
		k+=1


