from django import forms
from .models import Nota


class NotasForm(forms.ModelForm):
    """
    Formulario para facilitar la creación y edición de productos.
    """

    class Meta: 
        #Espeficiar a que modelo está asociado el formulario
        model = Nota

        fields = [
            'titulo',
            'nota',
        ]

        labels = {
            'titulo':'Titulo',
            'nota':'Nota',
        }

        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'nota':forms.Textarea(attrs={'class':'form-control','rows':3}),
        }
    
    def __init__(self, *args, **kwargs):
        super(NotasForm, self).__init__(*args, **kwargs)
        self.fields['titulo'].error_messages = {'required': 'custom required message'}
        self.fields['nota'].error_messages = {'required': 'custom required message'}

        
#DESPUES DE ALEJA 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
    

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
