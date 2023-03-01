from PIL import Image
#image = Image.open('D:\c_pgrms\python_programming\projects\image_to_ascii_art\src\star-vector-icon.png')
from urllib.request import urlopen
url = "https://python-pillow.org/images/pillow-logo.png"
image = Image.open(urlopen(url))
width, height = image.size
aspect_ratio = height/width
new_width = 120
new_height = aspect_ratio * new_width * 0.55
image = image.resize((new_width,int(new_height)))
image = image.convert('L')
#ascii_char = [' ','.',':','-','=','+','*','#','%','@']
ascii_char = [' ',' ','.',':','i','l','w','W','@','@']
ascii_art = ' '

for y in range(image.height):
    for x in range(image.width):
        pixel_value = image.getpixel((x,y))
        ascii_art += ascii_char[int(pixel_value * len(ascii_char) /255 % len(ascii_char))]
    ascii_art += '\n'
print(ascii_art)    
with open('ascii_art.txt', 'w') as file:
    file.write(ascii_art)
