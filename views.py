from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse

from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Product


def tp(request):
	t=Product.objects.all()
	return render(request, 'mainpage/tp.html', {'form': t})
def aboutus(request):
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has been created')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



def db(request):
	print("working")
	return render(request)

	
def hello(request):
   return render(request, 'mainpage/hello.html',{})





def about(request):
	
	return render(request,'mainpage/about.html',{})



def viewproducts(request):
	return render(request,'mainpage/viewproducts.html',{})

def aboutus(request):
	return render(request,'mainpage/aboutus.html',{})
	
def login(request):
	return render(request,'mainpage/login.html',{})
	
def register(request):
	return render(request,'mainpage/register.html',{})
	
def cart(request):
	return render(request,'mainpage/cart.html',{})


