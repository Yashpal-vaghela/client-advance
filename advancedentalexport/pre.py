from blog.models import *

def allpage(request):
    event = Events.objects.all()
    product = Product.objects.all()
    latest = Blog.objects.all().order_by('-id')[:3]
    main = Blog.objects.filter(main3=True).first()

    context = {
        'event':event,
        'product':product,
        'latest':latest,
        'main':main,
    }
    return context