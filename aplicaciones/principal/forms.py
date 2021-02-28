from django import forms
from .models import Person

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'    # IF I WANT A SPECIFIC THING, SAY   (TUPLA)  --->  ('nombre','apellido',)