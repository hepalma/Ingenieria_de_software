from django import forms
from django.forms import ModelForm
from .models import reserva

class ReservaForm(ModelForm):

    class Meta:
        model = reserva
        fields = "__all__"