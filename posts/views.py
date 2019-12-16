#Django
from django.shortcuts import render #Funcion que toma un request

#Utilities
from datetime import datetime


posts=[
	{
		'tittle':'Mont Blanc',
		'user':{
			'name':'Yésica Cortés',
			'picture':'http://picsum.photos/60/60/?image=1027',
		},
		'timestamp':datetime.now().strftime('%d %b %Y - %H:%M hrs'),
		'photo':'http://picsum.photos/800/600?image=1036'
	},
	{
		'tittle':'Via lactea',
		'user':{
			'name':'Christian Van Der Henst',
			'picture':'http://picsum.photos/60/60/?image=1005',
		},
		'timestamp':datetime.now().strftime('%d %b %Y - %H:%M hrs'),
		'photo':'http://picsum.photos/800/600?image=903'
	},
	{
		'tittle':'Nuevo auditorio',
		'user':{
			'name':'Uriel (@Thepianartist)',
			'picture':'http://picsum.photos/60/60/?image=883',
		},
		'timestamp':datetime.now().strftime('%d %b %Y - %H:%M hrs'),
		'photo':'http://picsum.photos/800/600?image=1076'
	},
]

def listPosts(request):
	#show all posts
	return render(request,'feed.html',{'posts':posts})

'''content=[]
for post in posts:
	content.append("""
		<p> <strong>{name}</strong> </p>
		<p> <small>{name}-{timestamp}</small> </p>
		<figure> <img src="{picture}"/> </figure>
		""".format(**post))

return HttpResponse('<br>'.join(content))
'''