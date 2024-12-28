from django.db import models

class MpaaRatingsModels(models.Model):
    mpaaRatting_id = models.AutoField(primary_key=True)
    MpaaType = models.CharField(max_length=150,blank=True,null=True)
    MpaaLabel = models.CharField(max_length=150,blank=True,null=True)
    
    def __str__(self):
        return self.MpaaLabel