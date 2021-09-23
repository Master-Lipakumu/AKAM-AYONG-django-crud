from django import forms

from malade.models import Malade





class MaladeForm(forms.ModelForm):
    class meta():
        model = Malade
        fields = "__all__"