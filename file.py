import numpy as np
from PIL import Image
import skimage


def resize(file_name)
    image=Image.open(file_name)
    dimension=512
    height=image.size[0]
    width=image.size[1]
    image=image.resize([dimension,dimension])
    no_of_blocks=(dimension*dimension)/(8*8)
    max_limit=(no_of_blocks)**(1/2)
    array=np.asarray(image)
    return array



