from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'
        
class WebpageForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        #fields=['name','url'] 
        #exclude=['email']
        #exclude=['url']
        #exclude=('topic_name',)
        #exclude={'name'}
        help_texts={'name':'enter name','url':'enter link','email':'example@gmail.com'}
        labels={'topic_name':'TN','name':'NM'}
        widgets={'url':forms.PasswordInput,'name':forms.Textarea}
class AccessrecordForm(forms.ModelForm):
    class Meta:
        model=Accessrecord
        fields='__all__'


