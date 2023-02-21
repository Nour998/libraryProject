from django.db import models

# Create your models here.
class Book(models.Model):
      #00000 you have one choice to create a book without isbncode
      isbnCode = models.CharField(max_length=20,primary_key=True,default='00000')
      title = models.CharField(max_length=255)
      nbPage = models.PositiveBigIntegerField(null=True,blank=True)
      #null=True champ non obligatoire
      image=models.ImageField(upload_to='photo/book',null=True, blank=True)
      price=models.DecimalField(max_digits=5,decimal_places=2)  
      author=models.CharField(max_length=255)
      description=models.TextField()
      nbcopies=models.IntegerField(default=1)
      #the default release filed is the current date
      releaseDate=models.DateField(auto_now_add=True)
      #releaseDate=models.DateField(default=datetime.datetime.now)
      
      


