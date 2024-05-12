from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'gender', 'get_image')
    list_display_links = ('name',)
    search_fields = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px">')
        else:
            return mark_safe(f'<img src="{"https://ami.by/thumbs/getthumb.php?w%5Cu003d200%5Cu0026h%5Cu003d267%5Cu0026src%5Cu003dimages/catalogue/items/sofa_prestizh_02.jpg"}" width="100px">')

    get_image.short_description = 'Image'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size', 'created', 'category', 'slug', 'get_image')
    list_display_links = ('name',)
    search_fields = ('name', 'price', 'size', 'category')
    list_editable = ('price', 'size', 'category')
    prepopulated_fields = {'slug': ('name',)}

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px">')
        else:
            return mark_safe(f'<img src="{"https://ami.by/thumbs/getthumb.php?w%5Cu003d200%5Cu0026h%5Cu003d267%5Cu0026src%5Cu003dimages/catalogue/items/sofa_prestizh_02.jpg"}" width="100px">')

    get_image.short_description = 'Image'
