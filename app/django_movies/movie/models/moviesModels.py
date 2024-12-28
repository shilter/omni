from django.db import models
from .genresModels import GenresModels
from .mpaaratingModels import MpaaRatingsModels

class MoviesModels(models.Model):
    movies_id = models.AutoField(primary_key=True)
    moviesName = models.CharField(max_length=150,blank=True,unique=True)
    moviesDescription = models.TextField(max_length=150,blank=True,null=True)
    moviesFiles = models.FileField(upload_to='movies/')
    moviesImg = models.ImageField(upload_to='preview_images/')
    moviesDuration = models.IntegerField(max_length=10)
    moviesLanguage = models.TextField(blank=True,null=True)
    moviesUserRatings = models.FloatField(default=0.00)
    moviesGenres = models.ForeignKey(GenresModels, on_delete=models.CASCADE)
    moviesMpaaRating = models.ForeignKey(MpaaRatingsModels, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.moviesName

    