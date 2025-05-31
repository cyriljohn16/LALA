from django import forms
from .models import Record

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'quantity', 'description', 'date', 'capital', 'srp', 'total_sold']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
