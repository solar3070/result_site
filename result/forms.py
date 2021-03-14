from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['name', 'phone']

    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['name'].label = "이름"
      self.fields['phone'].label = "번호"
      self.fields['name'].widget.attrs.update({
        'class': 'form-name',
        'placeholder': '김동덕',
      })    
      self.fields['phone'].widget.attrs.update({
        'class': 'form-phone',
        'placeholder': '010-1234-1234',
      })    
