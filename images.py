from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
converted_img = img.convert('L')
converted_img.save("./formatted-images/grey.png", "png")
crooked = converted_img.rotate(90)
# resized = converted_img.resize((300, 300))
box = (100, 100, 400, 400)
region = converted_img.crop(box)
region.show()