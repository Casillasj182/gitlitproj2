import ffmpy
from ffmpy import FFmpeg
import sys
import os
from wand.image import Image
import imageio 

print("This is the gif maker!!!")
imagenum=int(input("How many images do you want to use?"))

    
## will ask user for input on amount of images
var1 = input("Please enter image name ") ## more input from user to get the name 
var2 = input("Please enter image name ")
var3 = input("Please enter image name ")
var4 = input("Please enter image name ")

finalvar1=var1+".jpg"
finalvar2=var2+".jpg"
finalvar3=var3+".jpg"
finalvar4=var4+".jpg"
with Image() as wand:
   
    with Image(filename=finalvar1) as one: ## this will add images into the sequence 
        wand.sequence.append(one) ## this will merge the images together
    with Image(filename=finalvar2) as two: ## this will add images into the sequence 
        wand.sequence.append(two)
    with Image(filename=finalvar3) as three: ## this will add images into the sequence 
        wand.sequence.append(three) ## this will merge the images together
    with Image(filename=finalvar4) as four: ## this will add images into the sequence 
        wand.sequence.append(four)
    # Create progressive delay for each frame
    for cursor in range(imagenum): ## loop for each image and set the delay between each image
        with wand.sequence[cursor] as frame:
            frame.delay = 10 * (cursor + 5)
    # Set layer type
    wand.type = 'optimize'
    wand.save(filename='finalimage.gif')
    print("Gif has been made")
