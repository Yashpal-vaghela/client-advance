from django.contrib import admin
from .models import *
# Register your models here.
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=['email', 'date', 'message']
    search_fields = ['email', 'name']



admin.site.register(NewsLetter)
admin.site.register(Review)

admin.site.register(Contact, ContactAdmin)
admin.site.register(InstaPost)
admin.site.register(STLFile)
admin.site.register(STLFileData)
