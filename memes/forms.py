from django import forms
from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS

from .models import UploadMeme


class UploadMemeForm(ModelForm):
    #meme = forms.FileField(label='Select a file', help_text='max. 42 megabytes')
    class Meta:
        model = UploadMeme
        fields = '__all__'
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
