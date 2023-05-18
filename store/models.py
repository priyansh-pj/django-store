from django.db import models
import uuid
# Create your models here.
class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    name = models.CharField(max_length=200,null=False,blank=False)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
class Item(models.Model):
    owner = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    name = models.CharField(max_length=200 , null=False, blank=False)
    description = models.TextField(null=True,blank=True)
    quantity = models.IntegerField(null=False,blank=False)

    def __str__(self):
        return self.name