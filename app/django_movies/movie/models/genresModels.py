from django.db import models

class GenresModels(models.Model):
    genres_id = models.AutoField(primary_key=True)
    GenresName = models.TextField(max_length=150,blank=True, null=True)
    
    def __str__(self):
        return self.GenresName