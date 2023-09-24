from django import forms
from .models import Shifts

class ShiftsForm(forms.ModelForm):
    """Form definition for Employee."""

    class Meta:
        """Meta definition for Employeeform."""

        model = Shifts
        fields = ('__all__') #Campos que quiero qué aparezcan para registrar. ej campos especifico [first_name, last_name, job, skills] o todos los campos ('__all__')
        widgets = {
            'dni': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingresar el dni'
                }
            ),
            'short_name': forms.TextInput(
                attrs = {
                    'placeholder': 'Ingresar apellido'
                }
            ),    
        }



