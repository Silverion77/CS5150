from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import generic

import ee

def error(request):
	print('Error in server')
	return Http404

class MapView(generic.View):
	def extract_layer(layer):
		print ('in extract')
		data = { 'This layer has been extracted':layer }
		return data

	def post(self, request):
		print(request.POST)
		layer = request.POST['layer_title'];

		print(layer)
		data = extract_layer(layer)
		print("Got data")

		return HttpResponse(json.dumps(data));

	def get(self, request):
		return render(request, 'land_server/map_display.html')

	