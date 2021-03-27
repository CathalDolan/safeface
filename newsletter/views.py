from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import NewsletterUser


def newsletter_signup(request):
    redirect_url = request.POST.get('redirect_url')

    if request.method == "POST":
        email = request.POST.get('newsletter_email')
        if email:
            check_email_address = NewsletterUser.objects.get_or_create(email=email)
            # check_email_address = get_object_or_404(NewsletterUser, email=email)
            if str(check_email_address) == str(email):
                messages.error(request, f'We\'re already sending our newsletter to {email}')
            else:
                new_entry = NewsletterUser(email=email)
                new_entry.save()
                messages.info(request, f'Thank you! We\'ll start sending our newsletter to {email} asap.')
        else:
            messages.error(request, 'Please add a valid email address.')

    return redirect(redirect_url)
