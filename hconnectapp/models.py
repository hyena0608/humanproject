from django.db import models
# Create your models here.


class Contest(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to ="", blank = True, null = True)

class Party(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to ="", blank = True, null = True)

class Hobby(models.Model):
    Party = models.ForeignKey(Party, on_delete=models.CASCADE)
    hobby = models.CharField(max_length=100)
