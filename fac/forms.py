from django import forms

from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['cedula','nombres','apellidos','direccion','email','celular1','celular2','tipo',
            'estado']
        exclude = ['usuarioModifica','fechaModificado','usuarioCrea','fechaCreacion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })