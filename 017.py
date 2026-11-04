import sys

from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "sodtumes.gif",save_all = True, sppend_images = [images[1]], duration = 200, loop = 0
)