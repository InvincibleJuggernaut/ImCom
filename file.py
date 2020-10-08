import numpy as np
from PIL import Image
import math

def resize():
    image=Image.open('abc.jpg')
    image=image.resize([512,512])
    array=np.array(image)
    return array

def find_average(array,limit):
    averaged_array=[]
    for i in range(0,limit,2):
        average=(array[i]+array[i+1])/2
        averaged_array.append(average)
    return averaged_array

def find_difference(averaged_array, original_array):
    limit=int(len(original_array)/2)
    for i in range(0,limit):
        difference=original_array[i]-averaged_array[i]
        averaged_array.append(difference)
    return averaged_array


