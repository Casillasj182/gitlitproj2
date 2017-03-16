##Names:Joel Casillas, Francisco Hernandez, Conrado Aguilar
##Date: 3/15/2017
##Project: Gif Maker
## Class: CST 205 Multimedia Design and Programming 
##Project 2
## This is a gif maker that takes in 8 images and it will creat a gif out of them
## https://github.com/Casillasj182/gitlitproj2.git
import ffmpy
from ffmpy import FFmpeg
import sys
import os
from wand.image import Image
import imageio 

print("This is the gif maker!!!")
imagenum=int(input("How many images do you want to use?: "))

    ## try to control speed and 
    
## will ask user for input on amount of images
var1 = input("Please enter image name: ") ## more input from user to get the name 
var2 = input("Please enter image name: ") ## storing them in the variable var1.. and etc
var3 = input("Please enter image name: ")
var4 = input("Please enter image name: ")
var5 = input("Please enter image name: ")
var6 = input("Please enter image name: ")
var7 = input("Please enter image name: ")
var8 = input("Please enter image name: ")


finalvar1=var1+".jpg" ## getting the input image name from user and adds .jpg to the end so it'll run
finalvar2=var2+".jpg" ## storing the sum of the var input and the jpg and stores it into finalvar1...etc
finalvar3=var3+".jpg"
finalvar4=var4+".jpg"
finalvar5=var5+".jpg"
finalvar6=var6+".jpg"
finalvar7=var7+".jpg"
finalvar8=var8+".jpg"

with Image() as wand:
   
    with Image(filename=finalvar1) as image1: ## this will add images into the sequence 
        wand.sequence.append(image1) ## this will merge the images together
    with Image(filename=finalvar2) as image2: ## this will add images into the sequence 
        wand.sequence.append(image2)
    with Image(filename=finalvar3) as image3: ## this will add images into the sequence 
        wand.sequence.append(image3) ## this will merge the images together
    with Image(filename=finalvar4) as image4: ## this will add images into the sequence 
        wand.sequence.append(image4)
    with Image(filename=finalvar5) as image5: ## this will add images into the sequence 
        wand.sequence.append(image5)
    with Image(filename=finalvar6) as image6: ## this will add images into the sequence 
        wand.sequence.append(image6)
    with Image(filename=finalvar7) as image7: ## this will add images into the sequence 
        wand.sequence.append(image7)
    with Image(filename=finalvar8) as image8: ## this will add images into the sequence 
        wand.sequence.append(image8)
    
    
    for cursor in range(imagenum): ## loop for each image and set the delay between each image
        with wand.sequence[cursor] as frame:
            frame.speed = 100 ## this controls the speed of frames
            ##* (cursor + 5)
    # Set layer type
    wand.type = 'optimize' ## this will optimize it to the gif
    wand.save(filename='finalimage.gif')## saves it as a gif
    print("Gif has been made")
    
