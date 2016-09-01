from reportlab.pdfgen import canvas
from django.http import HttpResponse
from cStringIO import StringIO


def hello_pdf(request):
    response = HttpResponse(mimetype = 'application/pdf')
    response['Content-Disposeition'] = 'attachment;filename = hello.pdf'
    
    temp = StringIO()
    
    p = canvas.Canvas(temp)
    
    p.drawString(100, 100, "hello world",)
    
    p.showPage()
    p.save()
    
    response.write(temp.getvalue())
    return response

