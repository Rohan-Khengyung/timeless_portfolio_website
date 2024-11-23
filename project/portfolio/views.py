from django.shortcuts import render
from django.core.mail import EmailMessage
from django.contrib import messages  # for flash messages
from .models import Images

def award(request):
    return render(request, 'award.html')

def blog(request):
    return render(request, 'blog.html')

def service(request):
    return render(request, 'services.html')

def home(request):
    context = {}
    images = Images.objects.all()
    context["images"] = images

    if request.method == "POST":
        # Retrieve form fields
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        # Basic form validation
        if not all([name, email, subject, message]):
            messages.error(request, "All fields are required.")
        else:
            # Prepare the email
            email_message = EmailMessage(
                subject=f"{name} : {subject}",
                body=message,
                to=['balddish635@gil.com'],
                headers={"Reply-To": email}
            )

            # Attempt to send the email and handle errors
            try:
                email_message.send()
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, "There was an error sending your message. Please try again later.")
                # Optionally log the error here for debugging

    return render(request, "index.html", context)
