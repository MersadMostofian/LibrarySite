from django import forms
from .models import Book

class addBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','author','publishers','publishDate','category','image')

class editBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','author','publishers','publishDate','category','image')