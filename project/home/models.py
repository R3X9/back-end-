from django.db import models

# Create your models here.
class Portfolio(models.Model):
    app = models.CharField(max_length=100)
    prodect =models.IntegerField()
    branding= models.CharField(max_length=150)
    BOOK=("FILE_BOOK","LIST_BOOK"),
    ("FILE_BOOK","LIST_BOOK"),
    books=models.CharField(max_length=150,choices=BOOK)

    def __str__(self):
        return self.app
    
class team (models.Model):
    address =models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    call = models.CharField(max_length=20)
    send = models.TextField()
    
    def __str__(self):
        return self.email