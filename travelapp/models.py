from django.db import models

# Create your models here.

class place(models.Model):
    name= models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class blog(models.Model):
    img1 = models.ImageField(upload_to='picture')
    date = models.IntegerField()
    day = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    content = models.TextField()

