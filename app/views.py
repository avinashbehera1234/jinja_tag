from django.shortcuts import render

# Create your views here.
def jinja_tag(request):
    d={'name':'Avinash','age':24}
    return render(request,'jinja_tag.html',d)
