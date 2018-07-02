from django.forms import ModelForm

from .models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['pattern', 'test_string']
