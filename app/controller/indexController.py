from django.shortcuts import render, HttpResponse

class indexController():

    def index (request):
        return render(request,'views/index/index.html')
        #return HttpResponse ('<h5>jhoan</h5>')