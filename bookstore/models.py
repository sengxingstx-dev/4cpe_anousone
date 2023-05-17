from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse




#User = get_user_model()


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)


    class Meta:
        swappable = 'AUTH_USER_MODEL'


class Department(models.Model):
    depname_la = models.CharField(max_length=100, null=True, blank=True)
    depname_en = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.depname_en} ({self.depname_la})'


class Major(models.Model):
    majname_la = models.CharField(max_length=100, null=True, blank=True)
    majname_en = models.CharField(max_length=100, null=True, blank=True)
    dep = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.majname_en} ({self.majname_la})'


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    desc = models.CharField(max_length=1000)
    uploaded_by = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.CharField(max_length=100, null=True, blank=True)
    pdf = models.FileField(upload_to='bookapp/pdfs/')
    cover = models.ImageField(upload_to='bookapp/covers/', null=True, blank=True)
    major = models.ForeignKey(Major, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)        


