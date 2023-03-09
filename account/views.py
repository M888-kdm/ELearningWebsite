from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.models import Group

# Create your views here.
    
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False) 
            instructors = Group.objects.get(name='Instructors')
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            instructors.user_set.add(new_user) 
            return redirect('course_list')
    else:
        user_form = UserRegistrationForm()
        
    return render(request, 'registration/register.html', {'user_form': user_form})
        
            