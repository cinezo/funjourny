from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL

# Create your models here.

class Game(models.Model):
    game_name = models.CharField(max_length=150)
    slug = models.SlugField(default="", null=False)
    thumbnail_path = models.ImageField(upload_to='images', null=True)
    script_path = models.CharField(max_length=60, null=True)
    
    def get_absolute_url(self):
        return reverse("game-detail", args=[self.id-1])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.game_name)
        super().save(*args, **kwargs)
    

class Ranking(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    game_overall_score = models.IntegerField(null=True)
