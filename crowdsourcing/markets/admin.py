from django.contrib import admin
from .models import Markets, Categories

admin.site.site_header = 'Markets app'
admin.site.site_title = 'App admin page'
admin.site.index_title = 'Welcome to the Markets app admin page'


class CategoriesInline(admin.TabularInline):
    model = Categories


class MarketsAdmin(admin.ModelAdmin):
    model = Markets
    inlines = [CategoriesInline]


admin.site.register(Markets, MarketsAdmin)


# Register your models here.
