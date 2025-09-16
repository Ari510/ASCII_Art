from PIL import Image
from mpmath.libmp import round_down

img = Image.open("ascii-pineapple.jpg")
print(img.mode, img.width, img.height, img.format)

img_matrix = []
for i in range(0, img.height):
    row = []
    for j in range(0, img.width):
        row.append(img.getpixel((j,i)))
    img_matrix.append(row)

print(len(img_matrix))
print(img_matrix[0][0])
for i in range(0, len(img_matrix)):
    for j in range(0, len(img_matrix)):
        img_matrix[i][j] = int((img_matrix[i][j][0] + img_matrix[i][j][1] + img_matrix[i][j][2])/3)

print(img_matrix[0][0])