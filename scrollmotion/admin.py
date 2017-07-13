from django.contrib import admin
from models import Image


class ImageAdmin(admin.ModelAdmin):
	list_display = ('user', 'image')
	fields = ('user', 'image')

admin.site.register(Image, ImageAdmin)
