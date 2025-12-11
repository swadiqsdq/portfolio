from django.db import models

# Create your models here.
class Profile(models.Model):
    professions = models.JSONField(default=list) 
    name = models.CharField(max_length=100)
    profilePhoto = models.ImageField(upload_to='images/',blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=12,blank=True, null=True)
    education = models.TextField()
    experience = models.TextField()
    location = models.CharField(max_length=255)
    github = models.URLField(blank=True,null=True)
    linkedin = models.URLField(blank=True,null=True)
    x = models.URLField(blank=True,null=True)
    stackoverflow = models.URLField(blank=True,null=True)



    def __str__(self):
        return self.name
    
class About(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='about')
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='AboutImage/',blank=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations')
    title = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    year = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences')
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=150)
    duration = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    details = models.JSONField(default=list,null=True)

    def __str__(self):
        return self.role


class Internship(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='internships')
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=150)
    duration = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    details = models.JSONField(default=list,null=True)

    def __str__(self):
        return self.company


class Skill(models.Model):
    CATEGORY_CHOICE = (
        ('BACKEND','Backend'),
        ('FRONTEND','Frontend'),
        ('OTHER','Other Skills')
        
    )
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='skill')
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICE,default='OTHER')
    item = models.CharField(max_length=50)
    proficiency = models.IntegerField(help_text='Proficiency level from 0 to 100',default=50)

    def __str__(self):
        return self.item

class Projects(models.Model):
    CATEGORY_CHOICE = (
        ('django','Django'),
        ('python','Python'),
        ('fullstack','Full Stack'),
        ('other','Other')
        )
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='projects')
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='projectImage/',blank=True)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICE)
    description = models.TextField()
    tech = models.CharField(default=list)
    features = models.CharField(default=list)
    link = models.URLField(blank=True,null=True)
    code = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    