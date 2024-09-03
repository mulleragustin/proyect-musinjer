from django import forms
from django.forms import inlineformset_factory
from .models import Socio, Grupo


class SocioForm(forms.ModelForm):
    fec_nac = forms.DateField(
        required=False,
        label=False,
        widget=forms.DateInput(
            attrs={"class": "form-control form-control-sm", "type": "date"}
        ),
    )
    direccion = forms.CharField(
        required=False,
        label=False,
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}),
    )
    celular = forms.IntegerField(
        required=False,
        label=False,
        widget=forms.NumberInput(attrs={"class": "form-control form-control-sm"}),
    )
    telefono = forms.IntegerField(
        required=False,
        label=False,
        widget=forms.NumberInput(attrs={"class": "form-control form-control-sm"}),
    )
    email = forms.EmailField(
        required=False,
        label=False,
        widget=forms.EmailInput(attrs={"class": "form-control form-control-sm"}),
    )
    dependencia = forms.CharField(
        required=False,
        label=False,
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}),
    )
    cargo = forms.CharField(
        required=False,
        label=False,
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}),
    )
    funcion = forms.CharField(
        required=False,
        label=False,
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}),
    )
    domicilio_laboral = forms.CharField(
        required=False,
        label=False,
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}),
    )
    telefono_laboral = forms.IntegerField(
        required=False,
        label=False,
        widget=forms.NumberInput(attrs={"class": "form-control form-control-sm"}),
    )
    estado = forms.ChoiceField(
        required=False,
        label=False,
        choices=[
            ('A', 'Activo'),
            ('S', 'Suspendido'),
            ('B', 'Baja'),
        ],
        widget=forms.Select(attrs={"class": "form-select form-select-sm"}),
    )

    class Meta:
        model = Socio
        fields = "__all__"
        exclude = ['created_by', 'modified_by', 'created_at', 'updated_at']
        widgets = {
            "socio_id": forms.NumberInput(
                attrs={"class": "form-control form-control-sm"}
            ),
            "dni": forms.NumberInput(attrs={"class": "form-control form-control-sm"}),
            'caracter': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "apellido": forms.TextInput(
                attrs={"class": "form-control form-control-sm"}
            ),
            "nombre": forms.TextInput(attrs={"class": "form-control form-control-sm"}),
            'sexo': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'estado_civil': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "localidad": forms.TextInput(
                attrs={"class": "form-control form-control-sm"}
            ),
            "telefono": forms.NumberInput(
                attrs={"class": "form-control form-control-sm"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(SocioForm, self).__init__(*args, **kwargs)
        if self.data:  # Verifica si el formulario ha sido enviado
            for field_name, field in self.fields.items():
                if self.errors.get(field_name):
                    field.widget.attrs["class"] += " is-invalid"
                else:
                    field.widget.attrs["class"] += " is-valid"
    
   


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = "__all__"
        widgets = {
            "dni_familiar": forms.NumberInput(
                attrs={"class": "form-control form-control-sm"}
            ),
            'parentesco': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            "apellido_familiar": forms.TextInput(
                attrs={"class": "form-control form-control-sm"}
            ),
            "nombre_familiar": forms.TextInput(
                attrs={"class": "form-control form-control-sm"}
            ),
        }


GrupoFormSet = inlineformset_factory(
    Socio, Grupo, form=GrupoForm, extra=1, can_delete=True
)

class FiltroSocioForm(forms.Form):
    socio_id = forms.IntegerField(
        required=False,
        label=False,
        widget=forms.NumberInput(attrs={"class": "form-control form-control-sm"}),
    )
    dni = forms.IntegerField(
        required=False,
        label=False,
        widget=forms.NumberInput(attrs={"class": "form-control form-control-sm"}),
    )
    apellido = forms.CharField(
        required=False,
        label=False,
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}),
    )
    nombre = forms.CharField(
        required=False,
        label=False,
        widget=forms.TextInput(attrs={"class": "form-control form-control-sm"}),
    )
    estado = forms.ChoiceField(
        required=False,
        label=False,
        choices=[
            ('', 'Seleccione un estado'),
            ('A', 'Activo'),
            ('S', 'Suspendido'),
            ('B', 'Baja'),
        ],
        widget=forms.Select(attrs={"class": "form-select form-select-sm"}),
    )

