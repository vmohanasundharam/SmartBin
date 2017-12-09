# -*- coding: utf-8 -*-

from random import randint
import smtplib
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import bin_info,fill_level_stats

@csrf_exempt
def index(request):
    return render(request, 'smartbin/index.html', {})

def viewbins(request):
    return render(request, 'smartbin/view_bins.html', {})

@csrf_exempt
def register(request):
	if request.method == "GET" :
		return render(request, 'smartbin/pages-blank.html', {})
	if request.method == "POST" :
		bin_id =  request.POST.get('bin_id')
        latitude =  float(request.POST.get('latitude'))
        longitude =  float(request.POST.get('longitude'))
        access_key =  request.POST.get('access_key')
        landmark = request.POST.get('landmark')

        try:
            res = bin_info.objects.get(bin_id=bin_id)
            return render(request, 'smartbin/pages-blank.html', {'required':'yes'})
        except:
             s = bin_info(bin_id=bin_id,latitude=latitude,longitude=longitude,access_key=access_key,land_mark=landmark)
             s.save()
             return HttpResponseRedirect(reverse('register'));
 
def map(request):

	if request.method == "GET" :
 		data = []
 		result_sets = bin_info.objects.all()
 		for result in result_sets:
 			markers = {}
 			markers['bin_id'] = result.bin_id
 			markers['latitude'] = result.latitude
 			markers['longitude'] = result.longitude
 			markers['current_level'] = result.current_level
 			print markers['bin_id']
 			data.append(markers)
 		return render(request, 'smartbin/map-google.html', {'datas':data})

def update_stats(request):
	
	if(request.method == "GET"):		
		
		key = request.GET.get('key')
		bin_id = request.GET.get('bin_id')
		bin_level = request.GET.get('bin_level')
		try:
			result = bin_info.objects.get(access_key = key,bin_id=bin_id)
			new_state = fill_level_stats(bin_id=bin_id,bin_level = bin_level)
			new_state.save()
			result.current_level = bin_level
			result.save()
			return render(request, 'smartbin/index.html', {})		
			
		except Exception as e:
			raise e
	else:
		print "out side"

def update(request):
	if request.method == "GET" :
		return render(request, 'smartbin/update_bin.html', {})

def shortest_path(request):
	if request.method == "GET" :
 		data = []
 		result_sets = bin_info.objects.all()
 		for result in result_sets:
 			markers = {}
 			markers['bin_id'] = result.bin_id
 			markers['latitude'] = result.latitude
 			markers['longitude'] = result.longitude
 			markers['current_level'] = result.current_level
 			print markers['bin_id']
 			data.append(markers)
 		return render(request, 'smartbin/shortest_path.html', {'datas':data})

def table(request):
	if request.method == "GET" :
 		data = []
 		attrib = []
 		result_sets = bin_info.objects.all()
 		for result in result_sets:
 			new_bin = {}
 			new_bin['land_mark'] = result.land_mark
 			new_bin['bin_id'] = result.bin_id
 			new_bin['current_level'] = result.current_level
 			
 			data.append(new_bin)
 		return render(request, 'smartbin/table.html', {'datas':data,"attrib":attrib})


def green_icon(request):
	image_data = open("/home/mohan/projects/webserver/myproject/smartbin/static/img/green.png", "rb").read()
	return HttpResponse(image_data, content_type = "image/png")

def red_icon(request):
	image_data = open("/home/mohan/projects/webserver/myproject/smartbin/static/img/red.png", "rb").read()
	return HttpResponse(image_data, content_type = "image/png")

def yellow_icon(request):
	image_data = open("/home/mohan/projects/webserver/myproject/smartbin/static/img/yellow.png", "rb").read()
	return HttpResponse(image_data, content_type = "image/png")


        
        