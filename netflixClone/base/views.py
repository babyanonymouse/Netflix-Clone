from django.shortcuts import redirect, render
from .forms import CustomAuthenticationForm


# Create your views here.
def home(request):
    
    return render(request, 'base/home.html')

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log the user in
            from django.contrib.auth import login
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'base/login.html', {'form': form})