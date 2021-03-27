from django.conf.urls import url
from django.urls import path

from newsletter import views


urlpatterns = [
    path('newsletter_signup/', views.newsletter_signup, name='newsletter_signup'),
]
