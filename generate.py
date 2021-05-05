# Import
import math
from PIL import Image, ImageDraw
import cv2
import random

w, h = 128, 128

# traning and validation date file path
outline_path = "outline_data"
filled_path = "filled_data"

for count in range(150):

    n = random.randint(0, 2)

    # creating new Image object
    img_outline = Image.new("RGB", (w, h))
    img_filled = Image.new("RGB", (w, h))

    draw_filled = ImageDraw.Draw(img_filled)
    draw_outline = ImageDraw.Draw(img_outline)

    # Generate random offset adn create xy coordinate
    offset_x = random.randint(5, 50)
    offset_y = random.randint(5, 50)
    coordinate = [(offset_x, offset_y), (128 - offset_x, 128 - offset_y)]

    if (n == 0):
        # create rectangle image
        draw_filled.rectangle(coordinate, fill="#FFFFFF", outline="#FFFFFF")
        draw_outline.rectangle(coordinate, outline="#FFFFFF")

        # convert to binary image (1 layer)
        img_outline = img_outline.convert("1")
        img_filled = img_filled.convert("1")

        # write the data into the folders
        img_outline.save(outline_path + "/" + str(count) + ".png")
        img_filled.save(filled_path + "/" + str(count) + ".png")

    elif (n == 1):
        # create ellipse
        draw_filled.ellipse(coordinate, fill="#FFFFFF", outline="#FFFFFF")
        draw_outline.ellipse(coordinate, outline="#FFFFFF")

        # convert to binary image (1 layer)
        img_outline = img_outline.convert("1")
        img_filled = img_filled.convert("1")

        # write the data into the folders
        img_outline.save(outline_path + "/" + str(count) + ".png")
        img_filled.save(filled_path + "/" + str(count) + ".png")

    # else:
    #     # create dot
    #     draw_filled.point([w/2, h/2], fill="#FFFFFF")
    #     draw_outline.point([w/2, h/2], fill="#FFFFFF")

    #     # convert to binary image (1 layer)
    #     img_outline = img_outline.convert("1")
    #     img_filled = img_filled.convert("1")

    #     # write the data into the folders
    #     img_outline.save(outline_path + "/" + str(count) + ".png")
    #     img_filled.save(filled_path + "/" + str(count) + ".png")

    else:
        # create ellipse
        draw_filled.ellipse(coordinate, fill="#FFFFFF", outline="#FFFFFF")
        draw_outline.ellipse(coordinate, outline="#FFFFFF")

        # convert to binary image (1 layer)
        img_outline = img_outline.convert("1")
        img_filled = img_filled.convert("1")

        # write the data into the folders
        img_outline.save(outline_path + "/" + str(count) + ".png")
        img_filled.save(filled_path + "/" + str(count) + ".png")