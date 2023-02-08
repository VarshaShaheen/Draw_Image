from PIL import Image

# Open the image
img = Image.open("rohit.jpg")

# Convert to grayscale
img = img.convert("L")

# Resize the image
img = img.resize((80, 60), Image.ANTIALIAS)

# Define characters for grayscale values
characters = ".111"

# Create a text representation of the image
text = ""
for y in range(img.size[1]):
    for x in range(img.size[0]):
        gray = img.getpixel((x, y))
        text += characters[int(gray / 255 * (len(characters) - 1))]
    text += "\n"

# Print the text representation
print(text)
