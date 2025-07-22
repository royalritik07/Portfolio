from django.db import models

# Create your models here.

class Person(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name