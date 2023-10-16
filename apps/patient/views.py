from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .models import User
from .forms import UserForm

# ----------- Vista para el formulario donde se dan de alta los afiliados. -----------
class NewUser(CreateView):
    model = User # Modelo de afiliado
    template_name = 'patient/crear-paciente.html' # Template declarado.
    form_class = UserForm # Forms.py
    success_url = reverse_lazy('users_app:success') # Al ejecutarse lo redirige a la página de success.

    def form_valid(self, form):
        type = form.cleaned_data.get('type') # Toma el tipo de afiliado puesto en el formulario.
        dni2 = form.cleaned_data.get('dni2') # Toma el dni del titular puesto en el formulario.
        # Si el tipo de afiliado es diferente a titular, valida que el dni titular ingresado corresponda a un afiliado previamente creado.
        if type != '0' and not User.objects.filter(dni=dni2).filter(type='0').exists(): # Filtros de busqueda
            form.add_error('dni2', 'No existe ningún afiliado con el DNI Titular ingresado.')  # Mensaje de error.

            # Redirige de nuevo a la página del formulario con el mensaje de error
            return self.render_to_response(self.get_context_data(form=form))

        return super().form_valid(form)

# ----------- Vista del success -----------
class SuccessView(TemplateView):
    template_name = "base/success.html"
