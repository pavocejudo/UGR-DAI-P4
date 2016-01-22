from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Bar(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    direccion = models.CharField(max_length=200)
    numero_visitas = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Bar, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre

class Tapas(models.Model):
    bar = models.ForeignKey(Bar)
    nombre = models.CharField(max_length=100)
    votos = models.IntegerField(default = 0)
    slug = models.SlugField()
    picture = models.ImageField(upload_to='bares/', blank = True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Tapas, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.nombre

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    website = models.URLField(blank = True)
    picture = models.ImageField(upload_to='profile_images', blank = True)

    def __unicode__(self):
        return self.user.username
