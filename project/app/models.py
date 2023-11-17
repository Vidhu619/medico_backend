from django.db import models

# Create your models here.
class Book(models.Model):
   title=models.CharField(max_length=200)
   Author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
   date=models.DateField()
   def __str__(self):
        return self.title


class Author(models.Model):
     name=models.CharField(max_length=20)
     age=models.IntegerField()

     def __str__(self):
        return self.name