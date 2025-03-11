from django.core.mail import send_mail
from django.shortcuts import render
from .models import Mail
# Create your views here.
def main(request):
    if request.method == "POST":
       if request.POST.get('name') and request.POST.get('mail') and request.POST.get('message'):
           mail = Mail()
           mail.name = request.POST.get('name')
           mail.mail = request.POST.get('mail')
           mail.message = request.POST.get('message')
           mail.save()
           send_mail(
               "Trial",
               " Welcome"+request.POST.get('name')+"    to our cafe",
               "eljokeryoussef768@gmail.com",
                         [request.POST.get('email')],
               fail_silently=False,


           )
           return render(request, "index.html")
    return render(request,"index.html")