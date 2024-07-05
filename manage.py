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
