#django
from django.http import HttpResponse

#utilities
from datetime import datetime


def hello_world(request):
	now = datetime.now().strftime('%d %b %Y - %H:%M')
	return HttpResponse('Current time is {}'.format(str(now)))

def hola(request):
	print(request)
	return HttpResponse('hi')