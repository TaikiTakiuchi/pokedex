from django.db import models

# Create your models here.

class PokeModel(models.Model):
    #title=models.CharField(max_length=100)
    #memo=models.TextField()
    
    def __str__(self):
        return self.title

class UploadImage(models.Model):
    image = models.ImageField(upload_to='img/')