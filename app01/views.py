from django.shortcuts import  render_to_response
#from app01.models import Book
from app01.forms import  ContactForm
from django.http.response import HttpResponse, HttpResponseRedirect
# Create your views here.
'''
def search_form(request):
    return render_to_response('search_from.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for :%r '%request.GET['q']
    
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) >20:
                errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains = q)
            return render_to_response('search_results.html',
                                  {'books':books,'query':q})
    else:
        return render_to_response('search_form.html',
                                  {'error':errors})
        
'''
def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data 
            send_mail(
                      cd['subject'],
                      cd['message'],
                      cd.get('email','noreply@example.com'),
                      ['siteowner@example.com'],
                      )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
                           inital = {'subject':'I love You site'}
                           )
    return render_to_response('contact_form.html',{'form':form})


            
    
    
    