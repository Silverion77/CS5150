from django.shortcuts import render

def home(request):
	return render(request, 'land_server/map_display.html') 