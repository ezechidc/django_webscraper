from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


from .forms import ContactForm

@login_required()
def contact(request):
    form = ContactForm(request.POST or None)
    sent = False
    if form.is_valid():
        contact_name = form.cleaned_data.get('contact_name')
        contact_email = form.cleaned_data.get('contact_email')
        message = form.cleaned_data.get('message')

        # send email message
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = "%s: %s via %s"%(
                contact_name,
                contact_email,
                message
            )
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)
        sent = True
    context = {'form': form, 'sent': sent}

    return render(request, 'contact/contact.html', context)

