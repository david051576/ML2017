import numpy as np
import ast

# Open the input files
f1 = open("matrixA.txt","r")
f2 = open("matrixB.txt","r")

# read strings
str1 = f1.readline()
str2 = f2.readline()
f1.close()
f2.close()

# Transfer strings into int arrays
list1 = eval(str1)
list2 = eval(str2)

# Transfer them into nparrays
array1 = np.array(list1,dtype=np.int32)
array2 = np.array(list2,dtype=np.int32)

# Do the math
array = np.dot(array1,array2)

# Tranfer nparrays into list and get sorted
list_after = sorted(array.tolist())

# Get the output file
text_file = open("ans_one.txt", "w")

for item in list_after:
    text_file.write(str(item) + "\n")

text_file.close()
        
