import numpy as np
from PIL import Image
import skimage

def resize(file_name):
    image=Image.open(file_name)
    dimension=512
    height=image.size[0]
    width=image.size[1]
    image=image.resize([dimension,dimension])
    no_of_blocks=(dimension*dimension)/(8*8)
    max_limit=(no_of_blocks)**(1/2)
    array=np.asarray(image)
    return array,max_limit,dimension,height,width

def init_matrix(x,y):
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
    blocks=skimage.util.view_as_blocks(array, block_shape=(8,8))
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
    return H

def matrix_product(array1, array2):
    product=init_matrix(8,8)
    if(len(str(array2))==0):
        for i in range(0,8):
            for j in range(0,8):
                product[i][j]=array1[i][j]*array2
        product=list2array(product)
        return product
    else:
        array1=list2array(array1)
        array2=list2array(array2)
        for k in range(0,8):
            for i in range(0,8):
                product[k][i]=0
                for j in range(0,8):
                    product[k][i]=product[k][i]+(array1[k][j]*array2[j][i])
        product=list2array(product)
        return product

def compression(x,y,H,tran_H,):
    for i in range(len(x)):
        for j in range(len(x)):
            m=matrix_product(tran_H,x[i][j])
            y[i][j]=matrix_product(m,H)

    return y

def transpose(list_name):
    b=init_matrix(8,8)
    for i in range(0,8):
        for j in range(0,8):
                b[j][i]=list_name[i][j]
    b=list2array(b)
    return b

array,maxo,dimension,orig_height,orig_width=resize('abc.jpg')
maxo=int(maxo)

x=array.shape[0]
y=array.shape[1]
red=init_matrix(x,y)
green=init_matrix(x,y)
blue=init_matrix(x,y)

red_component=separate_components(x,y,0,array,red)
green_component=separate_components(x,y,1,array,green)
blue_component=separate_components(x,y,2,array,blue)

red_component=list2array(red_component)
green_component=list2array(green_component)
blue_component=list2array(blue_component)

red_blocks=create_blocks(red_component)
green_blocks=create_blocks(green_component)
blue_blocks=create_blocks(blue_component)

H=transform_matrix()

compressed_red=init_matrix(maxo,maxo)
compressed_green=init_matrix(maxo,maxo)
compressed_blue=init_matrix(maxo,maxo)

H_transpose=transpose(H)
for i in range(len(red_blocks)):
    for j in range(0,len(red_blocks)):
        compressed_red[i][j]=matrix_product(matrix_product(H_transpose,red_blocks[i][j]),H)
for i in range(len(green_blocks)):
    for j in range(0, len(green_blocks)):
        compressed_green[i][j]=matrix_product(matrix_product(H_transpose,green_blocks[i][j]),H)
for i in range(len(blue_blocks)):
    for j in range(0, len(blue_blocks)):
        compressed_blue[i][j]=matrix_product(matrix_product(H_transpose,blue_blocks[i][j]),H)


compressed_red=list2array(compressed_red)
compressed_green=list2array(compressed_green)
compressed_blue=list2array(compressed_blue)

components_red=compressed_red.transpose(0,2,1,3).reshape(dimension,dimension)
components_green=compressed_green.transpose(0,2,1,3).reshape(dimension,dimension)
components_blue=compressed_blue.transpose(0,2,1,3).reshape(dimension,dimension)

compressed=[]
for i in range(0,x):
    compressed.append([])
    for j in range(0,y):
        compressed[i].append([])
        for k in range(0,3):
            compressed[i][j].append([])


for i in range(0,x):
    for j in range(0,y):
        compressed[i][j][0]=components_red[i][j]
        compressed[i][j][1]=components_green[i][j]
        compressed[i][j][2]=components_blue[i][j]

compressed=list2array(compressed)
compressed=compressed.astype(np.uint8)

image_compressed=Image.fromarray(compressed)
image_compressed=image_compressed.resize([orig_height,orig_width])

#-X-X-X-

decompressed_red=init_matrix(maxo,maxo)
decompressed_green=init_matrix(maxo,maxo)
decompressed_blue=init_matrix(maxo,maxo)

for i in range(len(red_blocks)):
    for j in range(len(red_blocks)):
        decompressed_red[i][j]=matrix_product(matrix_product(H,compressed_red[i][j]),H_transpose)
for i in range(len(green_blocks)):
    for j in range(len(green_blocks)):
        decompressed_green[i][j]=matrix_product(matrix_product(H,compressed_green[i][j]),H_transpose)
for i in range(len(blue_blocks)):
    for j in range(len(blue_blocks)):
        decompressed_blue[i][j]=matrix_product(matrix_product(H,compressed_blue[i][j]),H_transpose)

decompressed_red=list2array(decompressed_red)
decompressed_green=list2array(decompressed_green)
decompressed_blue=list2array(decompressed_blue)

red_components=decompressed_red.transpose(0,2,1,3).reshape(dimension,dimension)
green_components=decompressed_green.transpose(0,2,1,3).reshape(dimension,dimension)
blue_components=decompressed_blue.transpose(0,2,1,3).reshape(dimension,dimension)

decompressed=[]
for i in range(0,x):
    decompressed.append([])
    for j in range(0,y):
        decompressed[i].append([])
        for k in range(0,3):
            decompressed[i][j].append([])

for i in range(0,x):
    for j in range(0,y):
        decompressed[i][j][0]=red_components[i][j]
        decompressed[i][j][1]=green_components[i][j]
        decompressed[i][j][2]=blue_components[i][j]

decompressed=list2array(decompressed)
decompressed=decompressed.astype(np.uint8)

decompressed_img=Image.fromarray(decompressed)
decompressed_img=decompressed_img.resize([orig_height,orig_width])