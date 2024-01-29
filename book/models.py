from django.db import models

# Book model
class Book(models.Model):
    title=models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=50,unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title