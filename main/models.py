from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL

# Create your models here.

class Game(models.Model):
    game_name = models.CharField(max_length=150)
    slug = models.SlugField(default="", null=False)
    description = models.CharField(max_length=9999, null=True)
    thumbnail_path = models.ImageField(upload_to='images', null=True)
    script_path = models.CharField(max_length=60, null=True)
    
    def get_absolute_url(self):
        return reverse("game-detail", args=[self.id-1])
    
    def __str__(self):
        return f"{self.game_name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.game_name)
        super().save(*args, **kwargs)


class Ranking(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    game_overall_score = models.IntegerField(null=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.player}: {self.game_overall_score}"
    

class Category(models.Model):
    game_category = models.CharField(max_length=100)
    games = models.ManyToManyField(Game)
    slug = models.SlugField(default="", null=False, blank=True)
    
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.game_category)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("game_category", args=[self.id-1])
    
    def __str__(self):
        return f"{self.game_category}" 