from django.contrib import admin

from . models import Category,Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category, CategoryAdmin)

admin.site.register(Product)