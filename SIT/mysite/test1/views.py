from django.shortcuts import render

def index(request):
	return render(request, 'test1/site1.html')
def index2(request):
	remote_address = request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR')
	return render(request, 'test1/site2.html', locals())
# Create your views here.
