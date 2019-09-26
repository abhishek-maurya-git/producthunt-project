from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.TextField(max_length=255)
    pub_date = models.DateTimeField()
    url = models.TextField()
    body = models.TextField(max_length=500,default='')
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
