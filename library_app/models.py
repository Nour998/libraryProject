from django.db import models
from django.utils import timezone

# Create your models here.

class Addres(models.Model):
    #django alredy create an id filed for ech model
    #id= models.BigAutoField()
    number= models.PositiveIntegerField()
    stratName= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    postCode= models.PositiveIntegerField()

class Editor(models.Model):
    name= models.CharField(max_length=100,unique=True)
    website = models.URLField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    #blank=True champ  non obligatoire
    TelephoneNumber = models.CharField(max_length=20,null=True,blank=True)
    #description the relationship between editor and adress (1 TO 1)
    Addres=models.OneToOneField(Addres,on_delete=models.CASCADE,null=True,blank=True)

class Book(models.Model):
      #00000 you have one choice to create a book without isbncode
      isbnCode = models.CharField(max_length=20,primary_key=True,default='00000')
      title = models.CharField(max_length=255)
      nbPage = models.PositiveBigIntegerField(null=True,blank=True)
      #null=True champ non obligatoire
      image=models.ImageField(upload_to='photo/book',null=True, blank=True)
      price=models.DecimalField(max_digits=5,decimal_places=2,default=1)  
      description=models.TextField(null=True,blank=True)
      nbcopies=models.IntegerField(default=1)
      #the default release filed is the current date
      releaseDate=models.DateField(auto_now_add=True,null=True,blank=True)
      #describe the relationship between book and editor(n TO 1)
      editor=models.ForeignKey(Editor,on_delete=models.CASCADE,null=True,blank=True)

class Author(models.Model):
    #pass 
    name=  models.CharField(max_length=100)
    nationality=  models.CharField(max_length=100)
    description=  models.TextField(null=True,blank=True)
    #description the relationship between author and book (n to n)
    #writing is the name of association table
    writing=models.ManyToManyField(Book,related_name='authors_books')



