from PIL import Image
from mpmath.libmp import round_down

path = input("JPG-Image filepath: ")
img = Image.open(path)
max_size = (500, 500)  # fits inside this box
img.thumbnail(max_size, Image.LANCZOS)

characters = list("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
print(img.width, img.height, img.format)

img_matrix = []
for i in range(0, img.height):
    row = []
    for j in range(0, img.width):
        row.append(img.getpixel((j,i)))
    img_matrix.append(row)

print(len(img_matrix))
print(img_matrix[0][0])
for i in range(0, len(img_matrix)):
    for j in range(0, len(img_matrix[0])):
        img_matrix[i][j] = (img_matrix[i][j][0] + img_matrix[i][j][1] + img_matrix[i][j][2])/3
        if img_matrix[i][j] == 255:
            img_matrix[i][j] = 254
        img_matrix[i][j] = characters[int(img_matrix[i][j] // 3.923)]
        print(img_matrix[i][j], sep="", end="")
    print()

# We are using these 65 ASCII characters: `^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$
# 255/65 = 3,923...


# I was originally going to make the brightness values into integers but keeping them as floats
# will make this easier/better


