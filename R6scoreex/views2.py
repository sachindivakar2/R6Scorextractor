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

def index(request):
    return render(request, 'R6scoreex/home.html')


def simple_upload(request):
	 

    print "Entered simple_upload"
	
    if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		#print fs
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		s=settings.MEDIA_ROOT
		print(os.path.join(settings.MEDIA_ROOT,"T.bmp"))
		print s[:-5]
		print os.path.join(s[:-5],'R6scoreex\\static\\R6scoreex\\cropped\\uploads')
		
		return render(request, 'R6scoreex/Result.html', {
		'uploaded_file_url': uploaded_file_url
		
        })
    return render(request, 'R6scoreex/Result.html')
