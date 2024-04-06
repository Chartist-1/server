from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class tour(models.Model): 
    
    id = models.AutoField(unique=True, editable=False, primary_key=True)
    objectType= models.CharField(blank=False,default = 'TOUR')
    
    durationNights =models.IntegerField(blank=True, null=True)
    rating= models.FloatField(blank=True,null=True)
    promo = models.BooleanField(default=False, blank=False)
    popularity= models.FloatField(blank=True,null=True)
    destination = models.CharField(blank=True,null=True)
    
    themes = ArrayField(models.CharField(max_length=10, blank=True),size=8, default=[''])
    title =models.CharField(max_length = 200, null = True)
    type = models.CharField(blank = False, default='Тур')
    iscanbuy= models.BooleanField(blank =False, default = True) 
    price = models.CharField(blank = False, default = 0)
    destination =models.CharField(blank =False, null = True)
    hasAudioGuide = models.BooleanField(blank = False, default = False)
    russpassRecomendation = models.BooleanField(blank = False, null = False, default=False)

class tourist(models.Model):
    pass

class hotel(models.Model):
    pass

class review(models.Model):
    pass

    
    
    