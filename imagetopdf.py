#!/usr/bin/env python3
#By Dx55

from PIL import Image

#You can add more than one image without problem

im1 = Image.open("Image path")
im2 = Image.open("Image path")

#Creating the PDF file list of image (also here you can add more image)
im_list = [im2]

#Putting PDF file path
pdf1_filename = "final pdf file path"

#Saving PDF file
im1.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=im_list)
