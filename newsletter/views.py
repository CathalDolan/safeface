from django.shortcuts import render, redirect, get_object_or_404

from newsletter.models import NewsletterUser


def newsletter_signup(request):
    redirect_url = request.POST.get('redirect_url')

    if request.method == "POST":
        email = request.POST.get('newsletter_email')
        if email:
            check_email_address = NewsletterUser.objects.get(email=email)
            if str(check_email_address) == str(email):
                print("Email already exists")
            else:
                new_entry = NewsletterUser(email=email)
                new_entry.save()
                print("Email saved")
        else:
            print("Email No")

    return redirect(redirect_url)
