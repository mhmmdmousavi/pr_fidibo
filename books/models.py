from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=36)
    bio = models.TextField(blank= True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length= 36)

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=64)
    author = models.ManyToManyField(Author, related_name= 'Books')
    categories = models.ManyToManyField(Category, related_name= 'books')
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits= 10 , decimal_places= 2)
    published_date = models.DateField(null= True, blank = True)

    def __str__(self):
        return self.title
    
