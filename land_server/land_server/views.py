from django.shortcuts import render
from django.views import generic

import ee

class MapView(generic.View):
	def post(self, request):
		pass

	def get(self, request):
		return render(request, 'land_server/map_display.html')

	def extract_layer():
		pass