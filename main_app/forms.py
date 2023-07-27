from django.forms import ModelForm
from .models import Stream

class StreamForm(ModelForm):
  class Meta:
    model = Stream
    fields = ['date', 'time']