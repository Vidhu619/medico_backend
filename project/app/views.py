from django.shortcuts import render
from app.models import Book, Author
from django.views import generic

def index(request):
   
    num_books = Book.objects.all().count()
  
    num_authors = Author.objects.count()
    
    cont = {
        'num_books': num_books,
        'num_authors': num_authors,
    }

   
    return render(request, 'index.html', context=cont)



class BookListView(generic.ListView):
    model = Book
