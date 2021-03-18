from django.shortcuts import render


# Displays the User's Profile
def profile(request):
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
