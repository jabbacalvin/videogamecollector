from django.db import models
from django.urls import reverse

# Create your models here.
class VideoGame(models.Model):
  title = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  release_year = models.IntegerField()

  def __str__(self):
    return f'{self.title} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'videogame_id': self.id})
  
class Stream(models.Model):
  date = models.DateField('stream date')
  time = models.TimeField()
  # Create a videogame_id FK
  videogame = models.ForeignKey(VideoGame, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.time} on {self.date}"

  class Meta:
    ordering = ['-date']