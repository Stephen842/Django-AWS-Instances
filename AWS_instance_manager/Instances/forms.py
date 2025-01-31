from django import forms
from .models import MyUser

class UserForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8
    )

    class Meta:
        model = MyUser
        fields = ['name', 'username', 'email', 'phone']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 8:
            raise forms.ValidationError('Name must be 8 characters long or more')
        return name
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 8:
            raise forms.ValidationError('Username must be 8 characters long or more')
        if MyUser.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already taken...')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if len(email) < 8:
            raise forms.ValidationError('Email address must be 8 characters long')
        if MyUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email Address Already Registered...')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) < 8:
            raise forms.ValidationError('Phone number is too short')
        return phone

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        
        if len(password1) < 8:
            raise forms.ValidationError('Password is too short, it must be at least 8 characters.')
        
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class SigninForm(forms.Form):
    identifier = forms.CharField()
    password = forms.CharField()

    def clean_identifier(self):
        identifier = self.cleaned_data.get('identifier')
        if not identifier:
            raise forms.ValidationError('Please enter a username or email.')
        return identifier

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError('Please enter a password.')
        return password
