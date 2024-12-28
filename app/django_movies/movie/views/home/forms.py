from django import forms

class SearchMovieForms(forms.Form):
    movie_name = forms.CharField(label="Movies Name",max_length=255)
