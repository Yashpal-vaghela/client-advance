from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password': forms.PasswordInput(),
    }    

    
# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()
    
#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]

#     def save(self, commit =True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']

#         if commit:
#             user.save()
#         return user    
#     def __init__(self, *args, **kwargs):
#             super(RegisterForm, self).__init__(*args, **kwargs)
#             self.fields['username'].widget.attrs = {'class': 'form-control', 'placeholder':'Username without spaces', 'onkeyup':'userCheck()'}
#             self.fields['email'].widget.attrs = {'class': ' form-control' }
#             self.fields['password1'].widget.attrs = {'class': ' form-control' }
#             self.fields['password2'].widget.attrs = {'class': ' form-control', 'onkeyup': 'pwfun()' }
    

class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class STLForm(forms.ModelForm):
    class Meta:
        model = STLFile
        fields = '__all__'

class STLFileForm(forms.ModelForm):
    class Meta:
        model = STLFileData
        fields = '__all__'

