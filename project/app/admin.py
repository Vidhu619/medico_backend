from django.contrib import admin

# Register your models here.
from .models import Book,Author

# admin.site.register(Book)

# admin.site.register(Author)

@ admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
   list_display = ('name','age')

@ admin.register(Book)
class BookAdmin(admin.ModelAdmin):
   list_display = ('Author','title')