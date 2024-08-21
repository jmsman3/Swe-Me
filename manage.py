# Post + Edit + Delete 
from django.shortcuts import render , redirect
from . import forms 
from . import models
# Create your views here.
# ------------------------------------------------------
def add_post(request):
    if request.method =='POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect ('add_post')
    else:
        post_form = forms.PostForm()
    return render(request , 'add_post.html' , {'form' : post_form})
# ------------------------------------------------------

def edit_post(request ,id):
    post = models.Post.objects.get(pk = id)
    post_form = forms.PostForm(instance=post)
    if request.method =='POST':
        post_form = forms.PostForm(request.POST , instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect ('homepage')
    
    return render(request , 'add_post.html' , {'form' : post_form})

# ------------------------------------------------------
def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
# ------------------------------------------------------




#Category ,Profile ,author

from django.shortcuts import render , redirect
from . import forms
# Create your views here.
def add_category(request):
    if request.method == 'POST': #if user click submit button 
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    else:  # user normally website e gele blank form pabe
        category_form = forms.CategoryForm()
    return render ( request , 'add_category.html' , {'form' : category_form})


# ------------------------------------------------------
from django.shortcuts import render , redirect
from .import forms
# Create your views here.

def add_profile(request):
    if request.method =='POST':
        profile_form = forms.ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profile')
    else:
        profile_form = forms.ProfileForm()
    return render(request , 'add_profile.html' ,{'form' : profile_form})

# ------------------------------------------------------

from django.shortcuts import render , redirect
from .import forms
# Create your views here.
def add_author(request):
    if request.method == 'POST': 
        author_form = forms.AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect ('add_author')
    else:
        author_form = forms.AuthorForm()
    return render(request , 'add_author.html', {'form' : author_form})

#---------------------------------------------------------------

# signup + login + logout+ Profile + Password Change1 +  pass_change2 + change_user_data

from django.shortcuts import render , redirect 
from django.http import HttpResponse
from first_app.forms import RegistrationForm , ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm ,PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate , login ,logout , update_session_auth_hash

# Create your views here.


def home(request):
    return render( request , 'home.html')

def profile(request):
    return render( request , 'profile.html')

def signup(request):
    if not  request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                messages.success(request , 'Account created succcessfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = RegistrationForm()
        return render(request , 'signup.html' ,{'form' : form})
    else:
        return redirect('profile')
#---------------------------------------------------------------
def user_login(request):
    if not  request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request , data = request.POST) # user er kache theke data nelam
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name , password = userpass) #check kori user database e ase kina
                if user is not None:
                    login(request , user)
                    return redirect('profile') #profile page e redirect korbe
        else:
            form = AuthenticationForm()           
        return render (request , 'login.html' , {'form' : form})
    else:
        return redirect('profile')
            
#---------------------------------------------------------------
def profile(request):
    if   request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST , instance = request.user)
            if form.is_valid():
                messages.success(request , 'Account updated succcessfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUserData(instance = request.user)
        return render(request , 'profile.html' ,{'form' : form})
    else:
        return redirect('signup')
    

    #---------------------------------------------------------------

def user_logout(request):
    logout(request)
    return redirect('login')
#---------------------------------------------------------------
def pass_change(request):
    # return HttpResponse('hello world')
    if  request.user.is_authenticated:
        if request.method =='POST':
            form = PasswordChangeForm(user=request.user ,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request , form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user= request.user)
        return render(request , 'passchange.html' , {'form' : form})
    else:
        return redirect('login')
    #---------------------------------------------------------------

def pass_change2(request):
    # return HttpResponse('hello world')
    if  request.user.is_authenticated:
        if request.method =='POST':
            form = SetPasswordForm(user=request.user ,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request , form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user= request.user)
        return render(request , 'passchange.html' , {'form' : form})
    else:
        return redirect('login')
    
#---------------------------------------------------------------
def change_user_data(request):
    if   request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST , instance = request.user)
            if form.is_valid():
                messages.success(request , 'Account updated succcessfully')
                form.save()
                print(form.cleaned_data)
        else:
            form = ChangeUserData(instance = request.user)
        return render(request , 'profile.html' ,{'form' : form})
    else:
        return redirect('signup')

# Get requirements.txt without version ,only just name :
# first command :-  pip freeze > requirements.txt
# second command to remove digit format version : - pip freeze | sed 's/==.*//' > requirements.txt

