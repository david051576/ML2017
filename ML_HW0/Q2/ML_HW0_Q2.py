import numpy as np
from PIL import Image

# read the png file using PIL
image1 = Image.open('lena.png')
image2 = Image.open('lena_modified.png')

array1 = np.array(image1,dtype=np.uint8)
array2 = np.array(image2,dtype=np.uint8)

array_output = np.ones((len(array1),len(array1[0]),4),dtype=np.uint8)

for i in range(0,len(array1)):
    for j in range(0,len(array1[0])):
        if (array1[i][j] != array2[i][j]).all():
            array_output[i][j] = array2[i][j]

img = Image.fromarray(array_output, 'RGBA')
img.save("ans_two.png")
