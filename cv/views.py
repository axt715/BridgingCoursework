from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from cv.forms import *


def cv(request):
    personalDetails = PersonalDetails.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    interests = Interests.objects.all()

    return render(request, 'blog.html', {'personalDetails': personalDetails, 'education': education, 'experience': experience, 'interests': interests})



# PERSONAL DETAILS EDIT
def personalDetails_edit(request):
    post = PersonalDetails.objects.first()
    if request.method == "POST":
        form = PersonalDetailsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = PersonalDetailsForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'Edit Personal Details'})



# EDUCATION EDIT
def education_edit(request, pk):
    post = get_object_or_404(Experience, pk=pk)
    if request.method == "POST":
        form = EducationForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = EducationForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'Edit Education'})

def education_new(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = EducationForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'New Education'})

def education_remove(request, pk):
    post = get_object_or_404(Education, pk=pk)
    post.delete()
    return redirect('/cv')



# EXPERIENCE EDIT
def exp_edit(request, pk):
    post = get_object_or_404(Qualification, pk=pk)
    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = ExperienceForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'Edit Experience'})

def exp_new(request):
    if request.method == "POST":
        form = ExperienceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = ExperienceForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'New Experience'})

def exp_remove(request, pk):
    post = get_object_or_404(Experience, pk=pk)
    post.delete()
    return redirect('/cv')



# INTERESTS EDIT
def interests_edit(request):
    post = Interests.objects.first()
    if request.method == "POST":
        form = InterestsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = InterestsForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'Edit Interests'})

def interests_new(request):
    if request.method == "POST":
        form = InterestsForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/cv')
    else:
        form = InterestsForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'name': 'New Interest'})


