import json
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse, FileResponse, Http404
from blog.models import *
from enquiry.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from enquiry.forms import STLForm, STLFileForm, LoginForm
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
import requests

# from enquiry.models import InstaPost
# Create your views here.


def api_user_login(request):
    if request.method == "POST":
        # your sign in logic goes here
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            #authenticate checks if credentials exists in db
            print(username, password)
            apiurl = 'https://export.adesurat.com//API.php?call=login'
            apiurl = str(apiurl)
            data = {
                "username": username,
                "password": password
            }
            
            print(apiurl)
            res = requests.post(apiurl, data=data)
            dict_data = res.json()
            login_success = (dict_data['status'])
            login_success = str(login_success)
            if login_success == "True":
                token = (dict_data['token'])
                token = str(token)
                
                user = dict_data['user']
                ids = user['userid']
                ids = str(ids)
                
                pk = token
                fk = ids
                #order
                order_apiurl = 'https://export.adesurat.com//API.php?call=order_list_get_dr'
                order_apiurl = str(order_apiurl)

                headers = { 
                            'Accept-Language' : 'content-copied-from-myhttpheader',
                            'User-Agent':'content-copied-from-myhttpheader',
                            'Token': pk
                        }

                data = {
                    "ids": fk
                }


                
                res = requests.post(order_apiurl, headers=headers, data=data)
                dict_data = res.json()
                order_data = (dict_data['data'])
                order_key = []
                for i in order_data:
                    for key in i:
                        order_key.append(key)
                    break    

                
                #invoice
                payment_apiurl = 'https://export.adesurat.com//API.php?call=paymentloadData'
                payment_apiurl = str(payment_apiurl)
                res = requests.post(payment_apiurl, headers=headers, data=data)
                dict_data = res.json()
                
                payment_data = (dict_data['data'])
                
                payment_key = []
                for i in payment_data:
                    for key in i:
                        payment_key.append(key)
                    break    


                #invoice
                invoice_apiurl = 'https://export.adesurat.com//API.php?call=invoiceloadData'
                invoice_apiurl = str(invoice_apiurl)
                res = requests.post(invoice_apiurl, headers=headers, data=data)
                dict_data = res.json()
                
                invoice_data = (dict_data['data'])
                
                invoice_key = []
                for i in invoice_data:
                    for key in i:
                        invoice_key.append(key)
                    break    

                #statement
                statement_apiurl = 'https://export.adesurat.com//API.php?call=statementData'
                statement_apiurl = str(statement_apiurl)
                res = requests.post(statement_apiurl, headers=headers, data=data)
                dict_data = res.json()
                
                statement_data = (dict_data['data'])
                statement_key = []
                for i in statement_data:
                    for key in i:
                        statement_key.append(key)
                    break    
            
                stb = dict_data['TotalBalance']

                context = {
                    'order_data':order_data,
                    'order_key':order_key,
                    'payment_data':payment_data,
                    'payment_key':payment_key,
                    'invoice_data':invoice_data,
                    'invoice_key':invoice_key,
                    'statement_data':statement_data,
                    'statement_key':statement_key,
                    'pk':pk,
                    'did':fk,
                    'user':user,
                    'stb':stb,
                }
                return render(request, 'ext_api.html', context)

                # return redirect('home:ext_api',  pk=token, fk=ids)
            else:
                messages.error(request, 'Login Failed!')
                return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

            # user = authenticate(username=username, password=password)
            # if user is not None:
            #     if user.is_active:
            #         login(request, user)
            #         return redirect('home:dashboard')

            #     else:
            #         return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

                    
            # else:
            #     return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        
    context = {
    
    }
    return render(request, 'api_login.html', context)
    
# https://adesurat.com

def ext_api(request, pk, fk):
    
    #order
    order_apiurl = 'https://export.adesurat.com//API.php?call=order_list_get_dr'
    order_apiurl = str(order_apiurl)

    headers = { 
                'Accept-Language' : 'content-copied-from-myhttpheader',
                'User-Agent':'content-copied-from-myhttpheader',
                'Token': pk
            }

    data = {
        "ids": fk
    }


    
    res = requests.post(order_apiurl, headers=headers, data=data)
    dict_data = res.json()
    order_data = (dict_data['data'])
    order_key = []
    for i in order_data:
        for key in i:
            order_key.append(key)
        break    

    
    #invoice
    payment_apiurl = 'https://export.adesurat.com//API.php?call=paymentloadData'
    payment_apiurl = str(payment_apiurl)
    res = requests.post(payment_apiurl, headers=headers, data=data)
    dict_data = res.json()
    
    payment_data = (dict_data['data'])
    
    payment_key = []
    for i in payment_data:
        for key in i:
            payment_key.append(key)
        break    


    #invoice
    invoice_apiurl = 'https://export.adesurat.com//API.php?call=invoiceloadData'
    invoice_apiurl = str(invoice_apiurl)
    res = requests.post(invoice_apiurl, headers=headers, data=data)
    dict_data = res.json()
    
    invoice_data = (dict_data['data'])
    
    invoice_key = []
    for i in invoice_data:
        for key in i:
            invoice_key.append(key)
        break    

    #statement
    statement_apiurl = 'https://export.adesurat.com//API.php?call=statementData'
    statement_apiurl = str(statement_apiurl)
    res = requests.post(statement_apiurl, headers=headers, data=data)
    dict_data = res.json()
    
    statement_data = (dict_data['data'])
    print(statement_data)
    statement_key = []
    for i in statement_data:
        for key in i:
            statement_key.append(key)
        break    
    
    stb = dict_data['TotalBalance']
    

    context = {
        'order_data':order_data,
        'order_key':order_key,
        'payment_data':payment_data,
        'payment_key':payment_key,
        'invoice_data':invoice_data,
        'invoice_key':invoice_key,
        'statement_data':statement_data,
        'statement_key':statement_key,
        'pk':pk,
        'did':fk,
        'stb':stb,
    }
    return render(request, 'ext_api.html', context)


def api_logout(request, pk, did):
    order_apiurl = 'https://export.adesurat.com//API.php?call=logout'
    order_apiurl = str(order_apiurl)
    headers = { 
                'Accept-Language' : 'content-copied-from-myhttpheader',
                'User-Agent':'content-copied-from-myhttpheader',
                'Token': pk
            }

    data = {
        "did": did
    }
    return redirect('home:api_user_login')


def print_order(request):
    if request.method == 'GET':
        #order
        fk = request.GET.get('token')
        order_no = request.GET.get('orderNo')
        order_apiurl = 'https://export.adesurat.com//API.php?call=orderprint'
        order_apiurl = str(order_apiurl)
       
        headers = { 
                    'Accept-Language' : 'content-copied-from-myhttpheader',
                    'User-Agent':'content-copied-from-myhttpheader',
                    'Token': fk
                }

        data = {
            "order_no": order_no
        }
    
        res = requests.post(order_apiurl, headers=headers, data=data)
        dict_data = res.json()
        
        link= str(dict_data['pdf_link'])
        context ={
            'link':link
        }
        return render(request, 'pdfview.html', context)
        # return redirect('home:home')

def print_payment(request):
    if request.method=='GET':
        doctor_id = request.GET.get('doctor_id')
        print(doctor_id)
        if doctor_id:
            pass
        else:
            doctor_id = ""    

        receipt_no = request.GET.get('receipt_no')
        if receipt_no:
            pass
        else:
            receipt_no = ""    
        
        amount = request.GET.get('amount')
        if amount:
            pass
        else:
            amount = ""   
        
        payment_mode = request.GET.get('payment_mode')
        if payment_mode:
            pass
        else:
            payment_mode = ""   
        
        
        chq_no = request.GET.get('chq_no')
        if chq_no:
            pass
        else:
            chq_no = "" 

        date = request.GET.get('date')
        if date:
            pass
        else:
            date = "" 

        fk = request.GET.get('token')
        if fk:
            pass
        else:
            fk = "" 
        print(fk)

        #order
        apiurl = 'https://export.adesurat.com//API.php?call=printpayment'
        apiurl = str(apiurl)
        
        headers = { 
                    'Accept-Language' : 'content-copied-from-myhttpheader',
                    'User-Agent':'content-copied-from-myhttpheader',
                    'Token': fk
                }

        data = {
            "doctor_id": doctor_id,
            "receipt_no":receipt_no,
            "amount":amount,
            "payment_mode":payment_mode,
            "chq_no":chq_no,
            'date':date
            
        }
        
        res = requests.post(apiurl, headers=headers, data=data)
        dict_data = res.json()
        data = dict_data
        link= str(dict_data['pdf_link'])
        context ={
            'link':link,
            'data':data,
        }
        return render(request, 'pdfview.html', context)
    
    # return redirect('home:home')

def print_statment(request, pk, did):
    #order
    apiurl = 'https://export.adesurat.com//API.php?call=printstatement'
    apiurl = str(apiurl)
    
    headers = { 
                'Accept-Language' : 'content-copied-from-myhttpheader',
                'User-Agent':'content-copied-from-myhttpheader',
                'Token': pk
            }

    data = {
        "doctor_id": did,
        
        
    }
    res = requests.post(apiurl, headers=headers, data=data)
    dict_data = res.json()
    
    link= str(dict_data['pdf_link'])
    context ={
        'link':link
    }
    return render(request, 'pdfview.html', context)
    
    # return redirect('home:home')

def print_invoice(request, pk, did):
    #order
    apiurl = 'https://export.adesurat.com//API.php?call=printinvoice'
    apiurl = str(apiurl)
    
    headers = { 
                'Accept-Language' : 'content-copied-from-myhttpheader',
                'User-Agent':'content-copied-from-myhttpheader',
                'Token': pk
            }

    data = {
        "invoice_ids": did,
        
        
    }
    res = requests.post(apiurl, headers=headers, data=data)
    dict_data = res.json()
    
    link= str(dict_data['pdf_link'])
    context ={
        'link':link
    }
    return render(request, 'pdfview.html', context)
    
    # return redirect('home:home')


