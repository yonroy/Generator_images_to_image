import cv2
from PIL import Image
from path_image import image_path
import numpy as np
from matplotlib import pyplot as plt

root_path = "./image/"
path_imgs = image_path(root_path)

# Read image generator
image_generator = Image.open("image_generator.jpg")

# 
slide_size = (1,1)

images = []
for path in path_imgs:
	image = Image.open(path)
	image = image.resize(slide_size,Image.ANTIALIAS)
	images.append( np.array(image))


def Generator_images_to_image(image_generator, images,slide_size):
    slide_width, slide_height = slide_size
    image_width, image_height = image_generator.size

    result = [[] for i in range(0, image_height, slide_height)]
    i= 0
    for y in range(0, image_height, slide_height):

        for x in range(0, image_width, slide_width):
            box = (x, y, x + slide_width, y + slide_height)
            slide = np.array(image_generator.crop(box))
            distance_image_to_image = list()
 
            for img in images:
            	distance_image_to_image.append(np.linalg.norm(slide - img))
            index = distance_image_to_image.index(max(distance_image_to_image))
            result[i].append(images[index])
            
        i+=1
    return result


images = Generator_images_to_image(image_generator,images,slide_size)
images = np.array(images)
shape = images.shape
plt.imshow(images.reshape(shape[0]*shape[2],shape[1]*shape[3],3))
plt.show()
