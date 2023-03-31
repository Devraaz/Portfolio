from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Blog
# Create your views here.

def index(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        message = request.POST.get('subject')
        

        contact = Contact(fname=fname, email = email, message = message, date=datetime.today())
        contact.save()
    return render(request, "index.html")
    #return HttpResponse('this is homepage')

def blog(request):
    blog = Blog.objects.all()

    param = {'blog': blog}


    return render(request, 'blog.html', param)

def project(request):
    return render(request, 'project.html')