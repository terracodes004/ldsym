from django.db import models

# Create your models here.
class Post(models.Model):
    date = models.DateField(auto_now_add=True)
    username = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    description = models.TextField()
    photos = models.FileField(max_length=3000)  # Adjusted to a reasonable max length
    a_approval = models.BooleanField()
    likes = models.IntegerField()
    comment = models.CharField(max_length=300)  # Adjusted to a reasonable max length
    hate = models.IntegerField()

class Scriptures(models.Model):
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()  # Use TextField for large content
    location = models.CharField(max_length=1000)
    file = models.FileField(upload_to=None, max_length=500)

class Faq(models.Model):
    name = models.CharField(max_length=500)
    title = models.CharField(max_length=50)
    comment = models.CharField(max_length=1000)  # Adjusted to a reasonable max length
    question = models.TextField()  # Use TextField for long questions
    file = models.FileField(max_length=500)

class News(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()

class Comments(models.Model):
    toname = models.CharField(max_length=500, blank=True)
    name = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    data = models.CharField(max_length=100)
    post_id = models.IntegerField(null=True, blank=True)  # Make post_id optional

class Likes(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    like = models.IntegerField()
    data = models.CharField(max_length=100)

class Hate(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    hate = models.IntegerField()  # Corrected to IntegerField()
    data = models.CharField(max_length=100)
class Udetails(models.Model):
    user = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    profile = models.FileField(max_length=500)
    des = models.TextField()
    tags = models.CharField(max_length=500)
    an_lds_ym = models.BooleanField(blank=True, null=True)