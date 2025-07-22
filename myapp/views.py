from django.shortcuts import render, redirect
from .models import Person
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def home(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        person = Person(full_name = full_name, email = email, message = message)
        person.save()

        # Send email to site admin
        send_mail(
            subject=f"New message form {full_name}",
            message=f"Name:{full_name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return redirect('/')

    

    return render(request, 'index.html')