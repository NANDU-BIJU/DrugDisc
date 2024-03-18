from django import forms
from .models import InputData

class InputDataForm(forms.ModelForm):
    class Meta:
        model = InputData
        fields = ['compound_name', 'smiles_notation']  # Add more fields as needed
