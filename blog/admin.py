from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=['h1']
    search_fields = ['title', 'h1', 'content','slug']


admin.site.register(Blog, BlogAdmin)

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Tags)
admin.site.register(MostPopularBlog)
admin.site.register(Events)
admin.site.register(EventsGallery)
admin.site.register(Product)
admin.site.register(SubProduct)
admin.site.register(Faqpage)
admin.site.register(Team)
admin.site.register(Testimonials)
admin.site.register(AboutImage)
admin.site.register(Client)
admin.site.register(Gallery)

admin.site.register(VideoTestimonals)