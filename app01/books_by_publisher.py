from django.shortcuts import get_object_or_404
from django.views.generic import list_detail
from app01.models import Book,Publisher, Author
import datetime




def book_by_publisher(request,name):
    publisher = get_object_or_404(Publisher,name__iexact = name)
    return list_detail.object_list(
                request,
                queryset =Book.objects.filter(publisher=publisher),
                template_name = 'app01/books_by_publisher.html',
                template_object_name = 'book',
                extra_context = {'publisher':publisher}
                 )
def author_detail(request,author_id):
    response = list_detail.object_detail(
                request,
                queryset = Author.objects.all(),
                object_id = author_id,
                )
    now = datetime.datetime.now()
    Author.objects.filter(id=author_id).update(last_accessed=now)
    
    return response

def author_list_plaintext(request):
    response = list_detail.object_list(
        request,
        quertset = Author.objects.all(),
        mimetype = 'text/plain',
        template_name = 'books/author_list.txt'
        )
    response["Content-Disposition"] = "attachment;filename = authors.txt"
    return response