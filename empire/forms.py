from django import forms 
from . models import *







class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['commenter','post','status']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = ['first_name', 'last_name', 'email', 'message']

