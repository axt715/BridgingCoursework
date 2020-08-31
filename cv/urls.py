from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv, name='cv'),
    # PERSONAL DETAILS
    path('personaldetails/edit', views.personalDetails_edit, name='personalDetails_edit'),

    # EDUCATION
    path('education/<int:pk>/edit', views.education_edit, name='education_edit'),
    path('education/<int:pk>/remove', views.education_remove, name='education_remove'),
    path('education/new', views.education_new, name='education_new'),

    # EXPERIENCE
    path('experience/<int:pk>/edit', views.exp_edit, name='exp_edit'),
    path('experience/<int:pk>/remove', views.exp_remove, name='exp_remove'),
    path('experience/new', views.exp_new, name='exp_new'),

    # INTERESTS
    path('interests/edit', views.interests_edit, name='interests_edit'),
    path('interests/new', views.interests_new, name='interests_new')
]