from django.contrib.auth.models import User
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    borrowed_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )

    @property
    def status(self):
        return "Borrowed" if self.borrowed_by is not None else "Available"

    def __str__(self):
        return self.title
