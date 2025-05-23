from django.shortcuts import render
from django.http import Http404, HttpResponse
from .forms import ContactForm

def home_page(request):
    context = {
        'message': 'Hi dude'
    }
    return render(request, 'home_page.html', context)
def about_us(request):
    context = {
        'message' : "Hi this is a test"
    }
    return render(request, 'home_page.html', context)


def contact_us(request):
    #    return HttpResponse('Hi this is Http res')
     contact_form = ContactForm()

     if request.method == "POST":
         print(request.POST.get("fullname"))
         print(request.POST.get("email"))
         print(request.POST.get("message"))
     context = {
         'message' : 'This is contact us page',
          'contact_form' : contact_form
     }
     return render(request, 'contact_us.html', context)



