from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20, blank=True)
    cel = models.CharField(max_length=15)
    mail = models.EmailField()
    register_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    # photo = models.ImageField(blank=True)
    categories = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


