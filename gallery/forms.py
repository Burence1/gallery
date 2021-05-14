from typing import FrozenSet
from django import forms
from django.db import models
from .models import Location,Category

class location_choices(forms.Form):
  location = forms.ModelChoiceField(queryset=Location.objects.all())