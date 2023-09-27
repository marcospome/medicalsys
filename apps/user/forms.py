from django import forms
from .models import User, Shifts

class ShiftsForm(forms.ModelForm):
    """Formulario para Shifts."""

    class Meta:
        """Metadatos del formulario."""

        model = Shifts
        fields = '__all__'  # Incluye todos los campos del modelo Shifts
        widgets = {
            'dni': forms.TextInput(attrs={'placeholder': 'Ingresar el DNI'}),
            'date': forms.TextInput(attrs={'placeholder': 'Ingresar la fecha: dd/mm/yy'}),
            
        }
    

    # ------------------- Validaciones -------------------
    # Validar por el DNI que el paciente exista.
    def clean_dni(self):
        dni = self.cleaned_data['dni']

        if not User.objects.filter(dni=dni).exists():
            raise forms.ValidationError('El DNI no corresponde a ningún cliente.')

        return dni
