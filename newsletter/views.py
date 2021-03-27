from django.shortcuts import render

from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm

def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        # Check to see if email address already exists
        if NewsletterUser.objects.filter(email=instance.email).exists():
            print("Sorry! This email exists")
        else:
            instance.save()

    context = {
        'form': form,
    }
    template = "newsletter/sign_up.html"
    return render(request, template, context)


def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        # Check to see if email address already exists
        if NewsletterUser.objects.filter(email=instance.email).exists():
            print("Sorry! This email exists")
        else:
            instance.save()

    context = {
        'form': form,
    }
    template = "newsletter/sign_up.html"
    return render(request, template, context)
