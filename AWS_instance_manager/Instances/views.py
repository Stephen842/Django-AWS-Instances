from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from .forms import UserForm, SigninForm # Import the form
from .models import MyUser
from .tasks import create_ec2_instance

def home(request):
    context = {
        'title': 'Your Personalized Dashboard'
    }
    return render(request, 'pages/home.html', context)

# To handle user's registration processes
class Signup(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'pages/signup.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            if user.username:  # Ensure username exists before modifying
                user.username = user.username.lower()  # Normalize username to lowercase
            user.save()

            # Trigger the Celery task asynchronously to create an EC2 instance for the new user
            #create_ec2_instance.delay(user.id)  # This will run in the background

            # Redirect the user to the login page after successful registration
            return redirect('login')
        
        return render(request, 'pages/signup.html', {'form': form})

# To handle user's authentication process with error handling capabilities
def Signin(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SigninForm(request.POST)

        if form.is_valid():
            identifier = form.cleaned_data['identifier']
            password = form.cleaned_data['password']

            # Check if the identifier is an email or username
            user = None
            if '@' in identifier:
                # It's an email
                try:
                    user = MyUser.objects.get(email=identifier)
                except MyUser.DoesNotExist:
                    user = None
            else:
                # It's a username
                try:
                    user = MyUser.objects.get(username=identifier)
                except MyUser.DoesNotExist:
                    user = None

            # Authenticate the user
            if user:
                user = authenticate(request, username=user.username, password=password)
                if user:
                    login(request, user)
                    return redirect('home')
                else:
                    form.add_error('password', 'Incorrect password. Please try again.')
            else:
                form.add_error('identifier', 'No user found with this email or username.')
    
    else:
        form = SigninForm()

    context = {
        'form': form,
        'title': 'Welcome Back! Sign In to Your Account',
        }
    return render(request, 'pages/signin.html', context)

# Handles user logout while keeping session data intact.
def logout(request):
    auth_logout(request)  # Logs out the user without clearing session data.
    return redirect('login') 