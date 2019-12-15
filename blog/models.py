from django.db import models
from datetime import datetime

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=300)
    create_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    

    def summary(self):
        return self.body[:100]

    def date_convertor(self):
        return self.create_date.strftime('%b %d %Y')