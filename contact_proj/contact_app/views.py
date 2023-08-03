from django.shortcuts import render,redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.http import HttpResponse,QueryDict
from .models import ContactUs

def contact_us(request):
    if request.method == 'GET':
        return render(request, 'contact.html')
    # elif request.method == 'POST':
    else:
        name = request.POST.get('name')
        email  = request.POST.get('email')
        phone = request.POST.get('phone')
        query = request.POST.get('query')

        contact = ContactUs(name=name, email=email, phone=phone, query=query)
        contact.save()

        message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nQuery: {query}"

        # Send email to company's team
        try:
            subject = 'Contact Form Submission'
            from_email = email
            send_mail(
                subject,
                message,
                from_email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )

            # Send reply email to the user
            reply_message = message = "Dear {},\n\nThank you for contacting us. We have received your inquiry and will respond shortly.\n\nBest regards,\XYZ".format(contact.name)
            subject = 'Thank you for contacting XYZ'
            send_mail(
                subject,
                reply_message,
                settings.DEFAULT_FROM_EMAIL,
                [from_email],
                fail_silently=False,
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        # request.POST = None
        request.POST = QueryDict('')
        return render(request, 'contact.html')