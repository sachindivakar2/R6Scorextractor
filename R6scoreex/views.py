# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.http import HttpResponse
import os
from django.conf import settings
import pdb;

import cv2
import numpy as np
import sys
import pytesseract
import os
from PIL import Image
import re
reload(sys)
sys.setdefaultencoding('utf-8')


def index(request):
    return render(request, 'R6scoreex/home.html')

"""def spaceRemover():
	s=settings.MEDIA_ROOT
	for i in range(1,13):
			
		with open(os.path.join(s[:-5],'R6scoreex','static','R6scoreex','extract',"B&W"+str(i)+".txt"),"r+") as file:
			for line in file:
				if not line.isspace():
					file.write(line)	
				"""
def extract(ilist):
	i=1 
	for img_cropped in ilist:
		
		img_cropped = cv2.bitwise_not(img_cropped)
		s=settings.MEDIA_ROOT
		cv2.imwrite(os.path.join(s[:-5],'R6scoreex','static','R6scoreex','cropped',"B&W"+str(i)+".png"), img_cropped)
		
		result = pytesseract.image_to_string(Image.open(os.path.join(s[:-5],'R6scoreex','static','R6scoreex','cropped',"B&W"+str(i)+".png")))

		lines = result.splitlines()
		filtered = [line for line in lines if line.strip()]
		new_output = '\n'.join(filtered)
		#[line for line in result.split('\n') if line.strip() != '']
		#filtered = filter(lambda x: not re.match(r'^\n\r$', x), result)
		f= open(os.path.join(s[:-5],'R6scoreex','static','R6scoreex','extract',"B&W"+str(i)+".txt"),"w")
		f.write(new_output)
		
		f.close()
		
		i+=1
		
def simple_upload(request):
	 

    print "Entered simple_upload"
	
    if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		#print fs
		if(fs.exists("T.bmp")):
			fs.delete("T.bmp")
			
		filename = fs.save("T.bmp", myfile)
		uploaded_file_url = fs.url(filename)
		s=settings.MEDIA_ROOT
		print s[:-5]
		print os.path.join(s[:-5],'R6scoreex\\static\\R6scoreex\\cropped\\uploads')
		
        
		# Read image with opencv
		print os.path.join(settings.MEDIA_ROOT,"T.bmp")
		
		img = cv2.imread(os.path.join(settings.MEDIA_ROOT,"T.bmp"))

		#print img.size
		#width , height = img.size

		#height,width,channel = img.shape
		height = img.shape[0]
		width  = img.shape[1]
		#print width,height
		ichl1=int(round(height*(.3009)))
		ichu1=int(round(height*(.5555)))
		icwl1=int(round(width*(.1770)))
		icwu1=int(round(width*(.3125)))

		ichl2=int(round(height*(.6481)))
		ichu2=int(round(height*(.8981)))
		icwl2=int(round(width*(.1770)))
		icwu2=int(round(width*(.3125)))


		icwl3=int(round(width*(.4687)))
		icwu3=int(round(width*(.5312)))

		icwl4=int(round(width*(.5520)))
		icwu4=int(round(width*(.625)))

		icwl5=int(round(width*(.6458)))
		icwu5=int(round(width*(.7187)))

		icwl6=int(round(width*(.75)))
		icwu6=int(round(width*(.8229)))

		icwl7=int(round(width*(.8437)))
		icwu7=int(round(width*(.9166)))

		icwl14=int(round(width*(.4687)))
		icwu14=int(round(width*(.9166)))

		ImgList = []

		img_cropped1 = img[ichl1:ichu1, icwl1:icwu1]           #crop_img(img, 0.64)
		ImgList.insert(0,img_cropped1)
		img_cropped2 = img[ichl2:ichu2, icwl2:icwu2] 
		ImgList.insert(1,img_cropped2)
		img_cropped3 = img[ichl1:ichu1, icwl3:icwu3]   
		ImgList.insert(2,img_cropped3)
		img_cropped4 = img[ichl1:ichu1, icwl4:icwu4]  
		ImgList.insert(3,img_cropped4)  
		img_cropped5 = img[ichl1:ichu1, icwl5:icwu5]   
		ImgList.insert(4,img_cropped5) 
		img_cropped6 = img[ichl1:ichu1, icwl6:icwu6]   
		ImgList.insert(5,img_cropped6) 
		img_cropped7 = img[ichl1:ichu1, icwl7:icwu7]        #crop_img(img, 0.64)
		ImgList.insert(6,img_cropped7) 

		img_cropped8 = img[ichl2:ichu2, icwl14:icwu14] 
		ImgList.insert(7,img_cropped8) 
		img_cropped9 = img[ichl2:ichu2, icwl3:icwu3]   
		ImgList.insert(8,img_cropped9) 
		img_cropped10 = img[ichl2:ichu2, icwl4:icwu4]    
		ImgList.insert(9,img_cropped10) 
		img_cropped11 = img[ichl2:ichu2, icwl5:icwu5] 
		ImgList.insert(10,img_cropped11)   
		img_cropped12 = img[ichl2:ichu2, icwl6:icwu6] 
		ImgList.insert(11,img_cropped12)    
		img_cropped13 = img[ichl2:ichu2, icwl7:icwu7]   
		ImgList.insert(12,img_cropped13) 

		#img_cropped14 = img[ichl1:ichu1, icwl14:icwl14] 


		#print len(ImgList)

		#print os.path.join(os.path.expanduser('~'),'uploads',"B&W"+"1"+".png")


		extract(ImgList)
		#spaceRemover()
		
		return render(request, 'R6scoreex/Result.html', {
		'uploaded_file_url': uploaded_file_url
		
        })
    return render(request, 'R6scoreex/Result.html')
