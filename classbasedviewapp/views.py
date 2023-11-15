from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
class getinput(View):
    def get(self,request):
        return  render(request,"getinput.html")
class postinput(View):
    def get(self,request):
        return render(request,"postinput.html")
class add(View):
    def get(self,request):
        i=request.GET["t1"]
        j=request.GET["t2"]
        try:
            x=int(i)
            y=int(j)
            z=x+y
            return HttpResponse("THE SUM IS:"+str(z))
        except(ValueError):
            return HttpResponse("INVALID DATA")
    def post(self,request):
        i=request.POST["t1"]
        j=request.POST["t2"]
        try:
            x=int(i)
            y=int(j)
            z=x+y
            return HttpResponse("THJE SUM IS:"+str(z))
        except(ValueError):
            return HttpResponse("INVALID DATA")
