# Generated by Django 5.1.4 on 2024-12-28 18:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenresModels',
            fields=[
                ('genres_id', models.AutoField(primary_key=True, serialize=False)),
                ('GenresName', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MpaaRatingsModels',
            fields=[
                ('mpaaRatting_id', models.AutoField(primary_key=True, serialize=False)),
                ('MpaaType', models.CharField(blank=True, max_length=150, null=True)),
                ('MpaaLabel', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoviesModels',
            fields=[
                ('movies_id', models.AutoField(primary_key=True, serialize=False)),
                ('moviesName', models.CharField(max_length=255)),
                ('moviesDescription', models.TextField(blank=True, null=True)),
                ('moviesFiles', models.FileField(upload_to='movies/')),
                ('moviesImg', models.ImageField(upload_to='preview_images/')),
                ('moviesDuration', models.IntegerField(max_length=10)),
                ('moviesLanguage', models.TextField(blank=True, null=True)),
                ('moviesUserRatings', models.FloatField(default=0.0)),
                ('moviesGenres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.genresmodels')),
                ('moviesMpaaRating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.mpaaratingsmodels')),
            ],
        ),
    ]