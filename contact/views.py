from django.shortcuts import render

# Create your views here.
def contact(request):
    """ A view to return the contact page"""
    context = {}
    return render(request, 'contact/contact.html', context)
