from django.db import models

# Create your models here.

class About (models.Model) : 
    about = models.TextField(max_length=1000)
    imqge = models.ImageField(upload_to='logo')
    fb_link = models.URLField(null=True,blank=True) 
    tw_link = models.URLField(null=True,blank=True)
    youtube_link = models.URLField(null=True,blank=True)
    inestagram_link = models.URLField(null=True,blank=True)
    def __str__(self):
        return self.about 

class Experience (models.Model) : 
    from_to = models.CharField(max_length=15)
    title = models.CharField(max_length=25)
    describtion = models.TextField(max_length=1000)
     def __str__(self):
        return self.title  

class Service (models.Model) : 
    icon = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    describtion = models.CharField(help_text=1000)
    def __str__ (self):
        return self.title 

class Projects (models.Model) : 
    title = models.CharField(max_length=100)
    imqge = models.CharField(upload_to='projects')
    subtitle = models.CharField(max_length=100)
    describtion = models.CharField(max_length=15000)
    def __str__ (self):
        return self.title

class Reviews (models.Model) : 
    name = models.CharField(max_length=30)
    job_title models.CharField(max_length=30)
    image = models.ImageField(upload_to='reviews')
    review = models.CharField(max_length=300)
    def __str__ (self):
        return self.name 

class Faq (models.Model) : 
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=400)
    def __str__ (self):
        return self.question  

class Contact (models.Model) : 
    name = models.CharField(max_length=100)
    email = models.EmailField()
    detail = models.TextField(max_length=500)
    def __str__ (self):
        return self.name 
