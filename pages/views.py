from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from categories.models import Category
from contact.forms import ContactForm


def index(request):
    categories = Category.objects.all().order_by('id').reverse()[:3]
    context = {
        'categories': categories,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html', {})

def thanks(request):
    return render(request, 'pages/thanks.html', {})

def services(request):
    return render(request, 'pages/services.html', {})

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            #Send email
            send_mail(
              'Contact Inquiry',
              'There has been an inquiry. Sign into the admin panel for more info.',
              'valentino.grancagnolo.com',
              ['valentino.grancagnolo.com'],
            )
            return thanks(request)

    return render(request, 'pages/contact.html', {'form': form})