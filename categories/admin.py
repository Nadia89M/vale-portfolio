from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id','name')
    search_fields = ('name', )
    list_per_page = 25

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = ("slug", )
        form = super(CategoryAdmin, self).get_form(request, obj, **kwargs)
        return form

admin.site.register(Category, CategoryAdmin)
