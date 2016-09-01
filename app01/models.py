from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length = 30)
    address = models.CharField(max_length = 50)
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length =30)
    country = models.CharField(max_length = 50)
    website = models.URLField()
    def __unicode__(self):
        return self.name
    
class Author(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    email = models.EmailField(blank = True,verbose_name = 'e-mail')
    def __unicode__(self):
        return u'%s %s' %(self.first_name,self.last_name)
    
    
class BookManager(models.Manager):
    def title_count(self,keyword):
        return self.filter(title__icontains = keyword).count()
        
class DahlBookManager(models.Manager):
    def get_query_set(self):
        return super(DahlBookManager,self).get_query_set().filter(auter='Road Dahl')

class Book(models.Model):
    title = models.CharField(max_length = 100)
    authors = models.ManyToManyField(Author)
    Publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True,null = True)
    mum_pages = models.IntegerField(blank=True ,null=True)
    objects = models.Manager()
    dahl_objects = DahlBookManager()
    
    
    def __unicode__(self):
        return self.title