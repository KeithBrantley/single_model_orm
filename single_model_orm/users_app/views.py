from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'index.html')

def process(requst):
    User.objects.create(
        first_name=request.POST["first_name"],
        last_name=request.POST["last_name"],
        email=request.POST["email_address"],
        age=request.POST["age"],
    )
    return redirect('/')