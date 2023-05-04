from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    website=models.URLField()
    report_id=models.CharField(max_length=20,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)