# -*- coding: utf-8 -*-
"""
@course:            CS 2302
@author:            Jorge Favela
@assignment:        Lab 2 
@instructor:        Dr. Olac Fuentes
Last Modified:      Mon Feb 17 02:08:39 2020
Purpose of program: Locate the brightest regions of solar photos
"""
import numpy as np
import matplotlib.pyplot as plt
import os

def read_image(imagefile):
    # Reads image in imagefile and returns color and gray-level images
    #
    img = (plt.imread(img_dir+file)*255).astype(int)
    img = img[:,:,:3]  # Remove transparency channel
    img_gl = np.mean(img,axis=2).astype(int)
    return img, img_gl

def draw_box(r,c,h,w,clr='r'):
    p= np.array([[r,c],[r,c+w],[r+h,c+w],[r+h,c],[r,c]])
    ax1.plot(p[:,1],p[:,0],linewidth=1,color=clr)
    ax2.plot(p[:,1],p[:,0],linewidth=1,color=clr) 
    
def brightest_pixel(I,h=100,w=100):
    row,column = np.where(I == np.amax(I)) #gets arrays of row and column indexes of the brightest pixesls in image
    draw_box(row[0]-(h/2),column[0]-(w/2),h,w,'b') #draws a blue square around the first brightest pixel located at its center

def compute_integral_img(I,m,n):
    s=np.zeros((m+1,n+1), dtype=int)
    s[1:,1:]= np.cumsum(np.cumsum(I,axis=1),axis=0) #array of cuma sum of I's rows and array of cuma sum of previus arrays columns gives us the intergal image of I
    return s
            
def integral_img_search(I,m,n,h,w):
    s = compute_integral_img(I,m,n) #computes the sum table of target image
    sums=0
    maxs=0 #holds the current highest sum value 
    r=0 #the current brightest regions top left corners coordinates in [row,column] format
    c=0
    for l in range(0,len(s)-h): #handles the shifting of the region vertically by 1
        for k in range(0,len(s[0])-w): #handles the shifting of the region horizontally by 1
            sums = (s[l+h,k+w])-(s[l,k+w])-(s[l+h,k])+(s[l,k]) #sum of the current region
            if sums>maxs:
                maxs = sums
                r=l-1
                c=k-1
    draw_box(r,c,h,w) #calls function to draw box around brightest region in image
    return r, c
 
def naive(I,m,n,h,w):
    maxs=0 #holds the current highest sum value 
    r=0 #the current brightest regions top left corners coordinates in [row,column] format
    c=0
    col_st=0 #these 2 variables are just here so they can exist outside any of the loops to be accessed after
    row_st=0
    for l in range(m-h,-1,-1): #handles the shifting of the region vertically by 1
        row_st=l #current regions row
        for k in range(n-w,-1,-1): #handles the shifting of the region horizontally by 1
            col_st=k #current regions column
            sums=0 #sum of the current region
            for i in range(row_st,row_st+h): # iterates through the current region
                for j in range(col_st,col_st+w):
                    sums+=I[i,j]
            if sums>maxs: #compares and updates brightest regions parameters if true
                maxs=sums
                r=row_st
                c=col_st
    draw_box(r,c,h,w) #calls function to draw box around brightest region in image
    return r, c
     
def naive_sum(I,m,n,h,w):
    maxs=0 #holds the current highest sum value 
    r=0 #the current brightest regions top left corners coordinates in [row,column] format
    c=0
    col_st=0 #these 2 variables are just here so they can exist outside any of the loops to be accessed after
    row_st=0
    for l in range(m-h,-1,-1): #handles the shifting of the region vertically by 1
        row_st=l #current regions row
        for k in range(n-w,-1,-1): #handles the shifting of the region horizontally by 1
            col_st=k #current regions column
            sums=np.sum(I[row_st:row_st+h,col_st:col_st+w])
            if sums>maxs: #compares and updates brightest regions parameters if true
                maxs=sums
                r=row_st
                c=col_st
    draw_box(r,c,h,w) #calls function to draw box around brightest region in image
    return r, c
1
inDir = input('Please enter directory containing target images: \n')    
img_dir = inDir # Directory where imagea are stored

img_files = os.listdir(img_dir)  # List of files in directory

plt.close('all')

for file in img_files:
    print(file)
    if file[-4:] == '.png': # File contains an image
        img, img_gl = read_image(img_dir+file)
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
        
        # naive(img_gl,len(img_gl),len(img_gl[0]),100,100)
        # naive(img_gl,len(img_gl),len(img_gl[0]),60,100)
        # naive(img_gl,len(img_gl),len(img_gl[0]),60,60)
        # naive(img_gl,len(img_gl),len(img_gl[0]),30,60)
        # naive(img_gl,len(img_gl),len(img_gl[0]),30,30)
        # naive(img_gl,len(img_gl),len(img_gl[0]),20,20)
        
        # naive_sum(img_gl,len(img_gl),len(img_gl[0]),100,100)
        # naive_sum(img_gl,len(img_gl),len(img_gl[0]),60,100)
        # naive_sum(img_gl,len(img_gl),len(img_gl[0]),60,60)
        # naive_sum(img_gl,len(img_gl),len(img_gl[0]),30,60)
        # naive_sum(img_gl,len(img_gl),len(img_gl[0]),30,30)
        # naive_sum(img_gl,len(img_gl),len(img_gl[0]),20,20)
        
        # integral_img_search(img_gl,len(img_gl),len(img_gl[0]),100,100)
        integral_img_search(img_gl,len(img_gl),len(img_gl[0]),60,100)
        # integral_img_search(img_gl,len(img_gl),len(img_gl[0]),60,60)
        # integral_img_search(img_gl,len(img_gl),len(img_gl[0]),30,60)
        # integral_img_search(img_gl,len(img_gl),len(img_gl[0]),30,30)
        # integral_img_search(img_gl,len(img_gl),len(img_gl[0]),20,20)


        brightest_pixel(img_gl,100,100)
        ax1.imshow(img)                  #Display color image
        ax2.imshow(img_gl,cmap='gray')   #Display gray-leval image
        plt.show()
        

