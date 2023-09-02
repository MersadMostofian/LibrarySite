from django.db import models

# Create your models here.
class Book(models.Model):
    name  = models.CharField(max_length=100)# Book Name 
    author = models.CharField(max_length=50)
    publishers = models.CharField(max_length=50)
    publishDate = models.IntegerField()
    cats  = [
        (1,'Historical Fiction'),

        (2,'Non-fiction'),

        (3,'Fiction'),

        (4,'Romance'),

        (5,'Science fiction'),

        (6,'Fantasy'),

        (7,'Horror'),

        (8,'Self-help book'),

        (9,'Memoir'),

        (10,'Young adult fiction'),

        (11,'Mystery'),

        (12,'Poetry'),

        (13,'Biography'),

        (14,'Literary fiction'),

        (15,'Thriller'),

        (16,"Children's literature"),

        (17,'Short stories'),

        (18,'Humor'),

        (19,'Autobiography'),

        (20,'Spirituality'),

        (21,'Graphic novel'),

        (22,'Classics'),

        (23,'Cookbook'),

        (24,'Action fiction'),
    ]
    category = models.IntegerField(choices=cats)
    image = models.ImageField(upload_to='images/')
    statusChoice = [
        ('Y','Not Trust'),
        ('N','Trust'),
    ]
    status = models.CharField(max_length=1,choices=statusChoice)# we can find status of book in our library
    given_to = models.CharField(max_length=50)# givent to {{ Username }}
