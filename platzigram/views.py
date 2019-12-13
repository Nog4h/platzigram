#django
from django.http import HttpResponse
from django.http import JsonResponse

#utilities
from datetime import datetime
import pdb


def hello_world(request):
	return HttpResponse('Current time is {}'.format(
		str(datetime.now().strftime('%d %b %Y - %H:%M'))
		))

def sortNumbers(request):
	#hi C:
	#pdb.set_trace()
	sortedNumbers= sorted([int(num) for num in request.GET['numbers'].split(',')])#creamos una lista y la ordenamos de menor a mayor
	data={
		'status' : 'ok', 
		'numbers': sortedNumbers,
		'message': 'Integers sorted succesfully'

	}
	return JsonResponse(data, safe= False)#retornamos la lista en formato json


def sayHi(request,name,age):
	#return a greeting
	if age < 12 : 
		message = 'Sorry {}, you are not allowed here'.format(name)
	else:
		message = 'Welcome {}, is nice to see you again.'.format(name)
	return HttpResponse(message)