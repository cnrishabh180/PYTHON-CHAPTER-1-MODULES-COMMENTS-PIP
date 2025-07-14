 # Label the program written in problem 4 with comments.

import os
#select the directory whose content u want to list 
directory = "."
#use the module to list the directory content
contents = os.listdir(directory)

print("Contents of the directory:", directory)



for item in contents:
    #print the content of directory
    print(item)
