from django import forms 
from .models import Topic, Entry 

class TopicForm(forms.ModelForm):
    """A class to allow users to add their topics"""
    class Meta:
        model = Topic 
        fields = ['text'] 
        labels = { 'text': ''} 

class EntryForm(forms.ModelForm):
    """A class to allow users to add learning log entries""" 
    class Meta:
        model = Entry
        fields = ['text'] 
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}