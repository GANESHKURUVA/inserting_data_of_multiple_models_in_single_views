from app.models import *
from django import forms


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=['name','email']


class AccessrecordsForm(forms.ModelForm):
    class Meta:
        model=Accessrecords
        fields=['author','date']