from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    available_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

