from django.contrib import admin
from mysite.books.models import Publisher, Author, Book
from mysite.myapp.models import *

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'testemail_1')
    search_fields = ('first_name', 'last_name')
    
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
#     fields = ('title', 'authors', 'publisher')  # Hidden some filed, make them un-editable
#     filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',)
        
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(News)
