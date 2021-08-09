from .models import Story
from django import forms
from ckeditor.fields import RichTextField
from django.db import models
from datetime import datetime

Choices = (('ComputerScience', 'ComputerScience'),
            ("Engineering", "Engineering"),
            ("Law", "Law"),
            ("Medicine", "Medicine"),
            ("Science", "Science"),
            ("Art", "Art"),
            ("Business", "Business"))

class StoryForm(forms.ModelForm):
    """
    This form is used for upload
    """
    title = forms.CharField(label='title', max_length=128,
                            widget=forms.TextInput(attrs={'placeholder': 'Please enter your title'})
                            )
    category = forms.ChoiceField(label='category', choices=Choices)
    text = RichTextField()
    img = models.ImageField(upload_to='img/', null=False)
    videoUrl = forms.URLField(label='videoUrl', max_length=512,
                              widget=forms.URLInput(attrs={'placeholder': 'Please enter your content'})
                              )
    paperLink = forms.URLField(label='paperLink', max_length=512,
                               widget=forms.URLInput(attrs={'Placeholder': 'Please enter your paper link'}))
    author = forms.CharField(label='author', max_length=100,
                             widget=forms.TextInput(attrs={'placeholder': 'Please enter author name'})
                             )
    author_intro = forms.CharField(label='author_intro', max_length=1000,
                                   widget=forms.TextInput(attrs={'placeholder': 'Please enter author introduction'})
                                   )
    background = forms.CharField(label='background', max_length=1000,
                                 widget=forms.TextInput(attrs={'placeholder': 'Please enter background introduction'})
                                 )
    tags = forms.CharField(label='tags', max_length=100,
                           widget=forms.TextInput(attrs={'placeholder': 'Please enter tags'})
                           )
    class Meta:
        model = Story
        fields = (
            'title',
            'category',
            'paperLink',
            'text',
            'img',
            'videoUrl',
            'author',
            'author_intro',
            'background',
            'tags',
        )


class AdvancedSearchForm(forms.Form):
    keyword = forms.CharField(label='title', max_length=9000,
                              widget=forms.TextInput(attrs={'placeholder': 'Contents you want to search'}),
                              required=False
                              )
    keyword_negate = forms.BooleanField(initial=False, required=False, label='Negate')

    operator1 = forms.ChoiceField(label='Operator', required=True, choices=(('AND', 'AND'), ('OR', 'OR')),
                                  widget=forms.Select(attrs={'class': 'query-operator'}))

    category = forms.ChoiceField(label='category',
                                 required=False,
                                 choices=(('All', 'All'),
                                          ('ComputerScience', 'ComputerScience'),
                                          ('Physics', 'Physics'),
                                          ("ElectricalEngineering", "ElectricalEngineering"),
                                          ),
                                 widget=forms.Select(attrs={'class': 'query-operator'}))
    category_negate = forms.BooleanField(initial=False, required=False, label='Negate')

    operator2 = forms.ChoiceField(label='Operator', required=True, choices=(('AND', 'AND'), ('OR', 'OR')),
                                  widget=forms.Select(attrs={'class': 'query-operator'}))

    start_at = forms.DateTimeField(label='start at', widget=forms.DateTimeInput(), initial=datetime.fromtimestamp(0),
                                   required=False)
    end_at = forms.DateTimeField(label='end at', widget=forms.DateTimeInput(), initial=datetime.fromtimestamp(9e9),
                                 required=False)
    time_negate = forms.BooleanField(initial=False, required=False, label='Negate')

    model = Story
    fields = (
        'keyword',
    )


class SearchForm(forms.Form):
    keyword = forms.CharField(label='title', max_length=9000,
                              widget=forms.TextInput(attrs={'placeholder': 'Contents you want to search'}),
                              required=False
                              )
    model = Story
    fields = (
        'keyword',
    )
