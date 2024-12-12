from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect 
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template

def byebye(request):
    logout(request)
    return redirect ('home:home')

def singup_user(request):
    
    user_form = RegisterForm()
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        if user_form.is_valid(): 
            username=user_form.cleaned_data['username']
            password=user_form.cleaned_data['password1']
            user = user_form.save()
            print(username)
            print(password)
            messages.success(request, 'Your profile was successfully created!')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if 'next' in request.POST:
                        return redirect('home:gp')
                    else:
                        return redirect('home:gp')
            else:
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))            

            
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
            

def login_user(request):
    
    if request.method == "POST":
        # your sign in logic goes here
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            #authenticate checks if credentials exists in db
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if 'next' in request.POST:
                        return redirect('home:gp')
                    else:
                        return redirect('home:gp')

                else:
                    return HttpResponse("Wait till verification")
                    
            else:
                messages.error(request, 'Invalid Credentails.')
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))          
    
    messages.error(request, 'Please correct the error below.')
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))          
                
    

# Create your views here.

def contactd(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            nam = request.POST.get('name')
            phone = request.POST.get('contact')
            message = request.POST.get('message')

            html_content = render_to_string ('contactmail.html',{ 
                'name':nam, 'phone':phone, 'message':message
            })
            email_from = settings.EMAIL_HOST_USER
            subject = 'New Data In STL Form'
            message = "You have a new data in STL form."
            recipient_list = ['stl@advancedentalexport.com']
            send_mail( subject, message, email_from, recipient_list, html_message=html_content, fail_silently=False )
            messages.success(request, 'Contact Details Sent Successfully')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))  

        else:
            messages.error(request, 'Please Try Again')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))  



def newsletter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Review Is Indexed Successfully')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))  

        else:
            messages.error(request, 'Please Try Again')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))  



def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Review Is Indexed Successfully')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))  

        else:
            messages.error(request, 'Please Try Again')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))  

