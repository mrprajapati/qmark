from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=60, null=False)
    email = models.EmailField(max_length=60)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
