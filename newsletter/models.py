from django.db import models


class NewsletterUser(models.Model):
    email = models.EmailField(default=False, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
