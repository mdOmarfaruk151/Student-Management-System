from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
            'email': forms.EmailInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'}),
            'phone_number': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md',
                'pattern': '[0-9]{11}'
            }),
            'course': forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-md'})
        }