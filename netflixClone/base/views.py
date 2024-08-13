from django.shortcuts import redirect, render
from .forms import CustomAuthenticationForm, SignupForm
from django.contrib.auth.decorators import login_required



# Create your views her
def home(request):
    
    return render(request, 'base/home.html')

@login_required
def dashboard(request):
    return render(request,'registration/dashboard.html',{'section':'dashboard'})


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in
            from django.contrib.auth import login
            user = form.get_user()
            login(request, user)
            return redirect('registration/dashboard')  
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'base/login.html', {'form': form})

def SignupView(request):
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../login/#')
    else:
        form = SignupForm()
     
    return render(request, 'base/signup.html', {'form': form})