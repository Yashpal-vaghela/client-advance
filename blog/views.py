from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blog_home(request):
    data1 = Blog.objects.all().order_by('-id')
    page = request.GET.get('page', 1)
    data2 =  Category.objects.all().order_by('-id')
    data3 = Blog.objects.filter(main3=True).order_by('-id')
    paginator = Paginator(data1, 9)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)


    context = {
        'data':data,
        'data2':data2,
        'data3':data3,
    }
    return render(request, 'blog_home.html', context)

# Create your views here.
def product_detail(request, pk):
    data = Product.objects.get(slug=pk)
    data2 =  SubProduct.objects.filter(product=data).order_by('-id')
    data3 = Blog.objects.filter(main3=True).order_by('-id')
    data4 = Faqpage.objects.filter(product=data).order_by('-id')
    
    context = {
        'data':data,
        'data2':data2,
        'data3':data3,
        'data4':data4,
    }
    return render(request, 'product_detail.html', context)


def blog_detail(request, pk):
    try:
        data = Blog.objects.get(slug=pk)
        blog_id = data.id
        data1 = Blog.objects.all().order_by('id')[:2]
        data2 =  Category.objects.all().order_by('-id')
        data3 = Blog.objects.filter(main3=True).order_by('-id')
        context = {
        'data':data,
        'data1':data1,
        'data2':data2,
        'data3':data3,
        }
        return render(request, 'blog_detail.html', context)

    except:
        data = Product.objects.get(slug=pk)
        data2 =  Category.objects.all().order_by('-id')
        data3 = Blog.objects.filter(main3=True).order_by('-id')
        data4 = Faqpage.objects.filter(product=data).order_by('-id')
        
        context = {
            'data':data,
            'data2':data2,
            'data3':data3,
            'data4':data4,
        }
        return render(request, 'product_detail.html', context)


    


def myblogsearch(request):
    print('here')
    if request.method=="GET":
        q = request.GET.get('q')
    else:
        q= "a"    
    print(q)
    data1 = Blog.objects.filter(content__contains=q).order_by('-id')
    if data1:
        page = request.GET.get('page', 1)
        paginator = Paginator(data1, 9)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

    else:
        data1 = Blog.objects.filter(content__contains="a").order_by('-id')
        page = request.GET.get('page', 1)
        paginator = Paginator(data1, 9)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
    data2 =  Category.objects.all().order_by('-id')
    data3 = Blog.objects.filter(main3=True).order_by('-id')
    context = {
        'data':data,
        'data2':data2,
        'data3':data3,
    }
    return render(request, 'blog_home.html', context)




def blog_list(request):
    data1 = Blog.objects.all().order_by('-id')
    page = request.GET.get('page', 1)

    
    paginator = Paginator(data1, 9)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)


    context = {
        'data':data,
    }
    return render(request, 'blog_list.html', context)

def cat_list(request, pk):
    
    data1 = Blog.objects.filter(category__id=pk).order_by('-id')
    page = request.GET.get('page', 1)

    
    paginator = Paginator(data1, 9)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)


    context = {
        'data':data,
    }
    return render(request, 'blog_list.html', context)


