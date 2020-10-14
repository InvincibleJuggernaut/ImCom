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

def init_3d_matrix(x,y):
    list_name=[]
    for i in range(0,x):
        list_name.append([])
        for j in range(0,y):
            list_name[i].append([])
    return list_name

def separate_components(x,y,k,array,list_name):
    for i in range(0,x):
        for j in range(0,y):
            list_name[i][j]=array[i][j][k]
    return list_name

def list2array(list_name):
    array=np.asarray(list_name)
    return array

def create_blocks(array):
    blocks=skimag.util.view_as_blocks(array, block_shape=(8,8))
    return blocks

def transform_matrix():
    B = [[0.35355, 0.35355, 0.50000, 0.00000, 0.70711, 0.00000, 0.00000, 0.00000],
         [0.35355, 0.35355, 0.50000, 0.00000, -0.70711, 0.00000, 0.00000, 0.00000],
         [0.35355, 0.35355, -0.50000, 0.00000, 0.00000, 0.70711, 0.00000, 0.00000],
         [0.35355, 0.35355, -0.50000, 0.00000, 0.00000, -0.70711, 0.00000, 0.00000],
         [0.35355, -0.35355, 0.00000, 0.50000, 0.00000, 0.00000, 0.70711, 0.00000],
         [0.35355, -0.35355, 0.00000, 0.50000, 0.00000, 0.00000, -0.70711, 0.00000],
         [0.35355, -0.35355, 0.00000, -0.50000, 0.00000, 0.00000, 0.00000, 0.70711],
         [0.35355, -0.35355, 0.00000, -0.50000, 0.00000, 0.00000, 0.00000, -0.70711]
         ]
    H=np.asarray(B)


array=resize(abc.jpg)

x=array.shape[0]
y=array.shape[1]
red=init_3d_matrix(x,y)
green=init_3d_matrix(x,y)
blue=init_3d_matrix(x,y)

red_component=separate_components(x,y,0,array,red)
green_component=separate_components(x,y,1,array,green)
blue_component=separate_components(x,y,2,array,blue)

red_component=list2array(red_component)
green_component=list2array(green_component)
blue_component=list2array(blue_component)

red_blocks=create_blocks(red_component)
green_blocks=create_blocks(green_component)
blue_blocks=create_blocks(blue_component)

transform_matrix()
