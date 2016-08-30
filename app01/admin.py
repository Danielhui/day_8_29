from django.contrib import admin
from models import Publisher,Author,Book

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','e-mail')
    search_fileds = ('first_name','last_name')
    
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publicatin_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    #fields = ('title','authors','publisher')
    filter_horizontal = ('authors',)
    raw_id_fields=('publisher',)

admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
