from PIL import Image

img = Image.open("ascii-pineapple.jpg")
print(img.mode, img.width, img.height, img.format)

img_matrix = []
for i in range(0, img.height):
    row = []
    for j in range(0, img.width):
        row.append(img.getpixel((j,i)))
    img_matrix.append(row)

print(len(img_matrix))

