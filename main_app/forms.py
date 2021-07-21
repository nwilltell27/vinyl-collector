from django.forms import ModelForm, fields
from .models import Touring

class TouringForm(ModelForm):
    class Meta:
        model = Touring
        fields = ['date', 'venue', 'city', 'state']