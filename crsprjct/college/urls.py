"""
URL configuration for crsprjct project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from college import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('login-check/', views.login_check, name='login-check'),
    path('signout/', views.signout, name='signout'),
    path('college-signup/', views.college_signup, name='college-signup'),
    path('company-signup/', views.company_signup, name='company-signup'),
    path('all-company/', views.all_company, name='all-company'),
    path('student-signup/', views.student_signup, name='student-signup'),
    path('add-vacancy-page/', views.add_vacancy_page, name='add-vacancy-page'),
    path('add-vacancy/', views.add_vacancy, name='add-vacancy'),
    path('all-vacancy/', views.all_vacancy, name='all-vacancy'),
    path('my-vac/', views.my_vac, name='my-vac'),
    path('forgot-password-page', views.forgot_password_page, name='forgot_password_page'),
    path('send-OTP', views.send_OTP, name='send_OTP'),
    path('reset-password', views.reset_password, name='reset_password'),
    path('fc-password', views.fc_password, name='fc-password'),
    path('profile/', views.profile, name='profile'),
    path('profile-update/', views.profile_update, name='profile-update'),
    path('view-profile/<int:pk>', views.view_profile, name='view-profile'),
    path('all-student/', views.all_student, name='all-student'),
    path('view-sprofile/<int:pk>', views.view_sprofile, name='view-sprofile'),
    path('privacy/', views.privacy, name='privacy'),
    path('update-privacy/', views.update_privacy, name='update-privacy'),
    path('add-suggesion-page/', views.add_suggesion_page, name='add-suggesion-page'),
    path('add-suggesion/', views.add_suggesion, name='add-suggesion'),
    path('all-suggesion/', views.all_suggesion, name='all-suggesion'),
    path('job-apply/<int:pk>', views.job_apply, name='job-apply'),
    path('applied-cand/', views.applied_cand, name='applied-cand'),
    path('view-resume/<int:pk>', views.view_resume, name='view-resume'),
    path('int-approval/<int:pk>', views.int_approval, name='int-approval'),
    path('approve/', views.approve, name='approve'),
    path('Schedules/', views.Schedules, name='Schedules'),

    path('emailajax/', views.emailajax, name='emailajax'),
]
