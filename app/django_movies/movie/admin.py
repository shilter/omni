from django.contrib import admin
from .models.genresModels import GenresModels
from .models.moviesModels import MoviesModels
from .models.mpaaratingModels import MpaaRatingsModels
# Register your models here.

admin.site.register(GenresModels)
admin.site.register(MoviesModels)
admin.site.register(MpaaRatingsModels)
