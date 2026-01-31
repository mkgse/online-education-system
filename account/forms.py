
from django import forms
from account.models import User



class SignUpForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirm_password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','email','phone_number']
        labels = {'first_name':'First Name','last_name':'Last Name' , 'email':'Email','phone_number':'Mobile'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'phone_number':forms.TextInput(attrs={'class':'form-control'})
        }

    def clean(self):
        cleaned_data = super(SignUpForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                "Password does not match!"
            )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "A user with this email already exists."
            )
        return email
        
class LoginForm(forms.ModelForm):
     class Meta:
          model = User
          fields = ['email','password']
          widgets = {
               'email':forms.EmailInput(attrs={'class':'form-control'}),
               'password':forms.PasswordInput(attrs={'class':'form-control'}),
          }