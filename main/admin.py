from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

# Register your models here.
admin.site.register(Ranking)
admin.site.register(Game)
admin.site.register(Category, CategoryAdmin)