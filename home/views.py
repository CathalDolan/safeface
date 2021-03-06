from django.shortcuts import render


# Return the index/home page
def index(request):
    return render(request, 'home/index.html')
