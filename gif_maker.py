import ffmpy
from ffmpy import FFmpeg
import sys

imagenum=int(input("How many images do you want to use?")) ## will ask user for input 
count=0 ## set the counter to zero so we can later increment
list=[] ## this will hold the input by the user 

while(imagenum > count): ## this will run depemding on the input of the user then it'll stop
    count=count+1 ## will increment by one 
    var = input("Please enter image name ") ## more input from user 

    finalimages=var+".jpg" ## will get the input image names and add .jpg to the end
    list.append(finalimages) ## this will append the list so all input is saved

print(list)


    
ff=ffmpy.FFmpeg(
    
    ##store list values into the input 
    inputs={list[0]: None}, ## this will input the 2 images I have
    ## have user enter output name .gif
   
    outputs={'image.gif': None}) ## this will take the 2 images and make a gif compiled of the 3 images
ff.run()
    
