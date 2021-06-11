from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm
from .models import UploadJokes, SearchModel
from django import forms

class UploadJokeForm(ModelForm):
    class Meta:
        exclude = ('votes', 'rating','tag', 'shares','pub_date')
        model = UploadJokes
        fields = '__all__'
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }

class SearchForm(ModelForm):
    search_term = forms.CharField(max_length=100)
    class Meta:
        model = SearchModel
        fields = '__all__'
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
#class ContactForm(forms.Form):
 #   subject = forms.CharField(max_length=100)
  #  message = forms.CharField(widget=forms.Textarea)
   # sender = forms.EmailField()
    #cc_myself = forms.BooleanField(required=False)
    

#class commentform(forms.Form):
#    comment = forms.CharField(max_length=100)

class sendMailForm(forms.Form):
    #Your_email_address = forms.EmailField()
    #message = forms.CharField(label='message', max_length = 1000)
    #summary = forms.CharField(max_length = 100)
    ananomyous_username = forms.CharField(label='ananomyous_username', max_length = 50)
    body = forms.CharField(label='body', max_length = 500)
    email = forms.EmailField()
