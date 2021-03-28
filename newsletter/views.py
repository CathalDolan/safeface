from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from .models import NewsletterUser


def newsletter_signup(request):
    redirect_url = request.POST.get('redirect_url')

    if request.method == "POST":
        email = request.POST.get('newsletter_email')
        if email:
            try:
                check_email_address = \
                    get_object_or_404(NewsletterUser, email=email)
                messages.error(request, f'We\'re \
                                    already sending our newsletter to {email}')
            except:
                new_entry = NewsletterUser(email=email)
                new_entry.save()
                messages.info(request, f'Thank you! We\'ll \
                                start sending our newsletter to {email} asap.')
        else:
            messages.error(request, 'Please add a valid email address.')

    return redirect(redirect_url)
