from django import forms
from django.forms import ModelForm
from .models import cliente

class ClienteForm(ModelForm):

    class Meta:
        model = cliente
        fields = "__all__"