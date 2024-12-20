from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home_view(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return redirect('login')


def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
        else:
            return render(request,'login.html',{'form':form})



def signup_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('home')
        else:
            return render(request,'signup.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('login')

