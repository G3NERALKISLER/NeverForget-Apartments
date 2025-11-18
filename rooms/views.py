from django.shortcuts import render, redirect
from .models import Category
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, "rooms/home.html")

def about(request):
    return render(request, 'rooms/about.html')

def vacancy(request):
    categories = Category.objects.all()
    return render(request, "rooms/vacancy.html", {"categories": categories})
from django.shortcuts import render, redirect
from .models import Category
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Home page
def home(request):
    return render(request, "rooms/home.html")

# About page
def about(request):
    return render(request, "rooms/about.html")

# Vacancy page
def vacancy(request):
    categories = Category.objects.all()
    return render(request, "rooms/vacancy.html", {"categories": categories})

# Contact page
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Subject includes sender's name
        subject = f"New Contact Form Submission from {name}"

        # Full message includes sender's email
        full_message = f"Sender: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,       # From your Gmail
                [settings.EMAIL_HOST_USER],     # To your Gmail (you receive it)
                fail_silently=False,
                     # So you can reply directly to the sender
            )
            messages.success(request, "Your message has been sent successfully ✅")
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")

        return redirect("contact")  # Redirect back to contact page

    return render(request, "rooms/contact.html")
