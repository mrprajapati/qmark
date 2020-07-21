from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form = Contact(name=name, email=email,
                       subject=subject, message=message)
        form.save()
        return HttpResponse('OK')
    return render(request, 'contact.html')
def low(self):
    pela = 'loweer'
    if pela == pela:
        return True
    else:
        return False
