from django.shortcuts import render
from django.http import Http404, HttpResponse



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
     context = {
         'message' : 'This is contact us page'
     }
     return render(request, 'contact_us.html', context)



