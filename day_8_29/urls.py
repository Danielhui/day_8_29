"""day_8_29 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
#from django.contrib import admin
from app01.models import Publisher,Book
from _csv import list_dialects
from app01 import books_by_publisher


def get_books():
    return Book.objects.all()

apress_books = {
             'queryset':Book.objects.order_by('-publication_date'),
             'template_name':'app01/apress_list.html'
             }

publisher_info = {
                  'queryset':Publisher.objects.all(),
                  'template_object_name':'publlisher',
                  'extra_context':{'book_list':Book.objects.all()}
                  }

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^hello/$',hello),
    #url(r'^time/$',current_datetime),
    #url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    #url(r'^search-form/$',views.search_form),
    #url(r'^search/$',views.search),
    url(r'^publishers/$',list_dialects.object_list,publisher_info),
    url(r'^books/(\w+)/$',books_by_publisher),
    url(r'^authors/(?P<author_id>\d+)/$', author_detail),

]
