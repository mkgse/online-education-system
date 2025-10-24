from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm  
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _ 
from .models import Addmissionform,Payment,Admission_Status,Feedback
from datetime import datetime,date


GENDER_CHOICES=[
     ('Male','Male'),
     ('Female','Female')
]
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name' , 'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'})
        }
class LoginForm(AuthenticationForm):
     username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
     password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))
class ChangeForm(PasswordChangeForm):
     old_password = forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))
     new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))
     new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'class':'form-control'})
     )


class AdmDetails(forms.ModelForm):
  
     gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
     class Meta:
          model = Addmissionform
          fields = ['firstname','middlename','lastname','fathername','mothername','dob','gender','mobile','email',
                 'address','city','state','pin','board','board1','board2','passing_year','passing_year1','passing_year2','percentage','percentage1'
          ,'percentage2','roll_number','roll_number1','roll_number2','photo','signature','matriculation','intermediate','graducation','postgraducation','address_proof','course_applied_for' ]
          labels={'firstname':'First Name','middlename':'Middle Name','lastname':'Last Name','fathername':'Father Name','mothername':'Mother Name',
                 'dob': 'Date of Birth','mobile':'Mobile','email':'Email',
                  'address':'Address','city':'City','state':'State','pin':'Pin Code'}
          widgets = {'firstname':forms.TextInput(attrs={'class':'form-control'}),
        'middlename':forms.TextInput(attrs={'class':'form-control'}),
        'lastname':forms.TextInput(attrs={'class':'form-control'}),
        'fathername':forms.TextInput(attrs={'class':'form-control'}),
        'mothername':forms.TextInput(attrs={'class':'form-control',}),
        'dob':forms.DateInput(attrs={'class':'form-control','id':'txtDate','placeholder': 'MM/DD/YYYY'}),
        'mobile':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'state':forms.Select(attrs={'class':'form-select'}),
        'pin':forms.NumberInput(attrs={'class':'form-control'}),
        'board':forms.TextInput(attrs={'class':'form-control'}),
        'board1':forms.TextInput(attrs={'class':'form-control'}),
        'board2':forms.TextInput(attrs={'class':'form-control'}),
        'passing_year':forms.TextInput(attrs={'class':'form-control'}),
        'passing_year1':forms.TextInput(attrs={'class':'form-control'}),
        'passing_year2':forms.TextInput(attrs={'class':'form-control'}),
        'percentage':forms.TextInput(attrs={'class':'form-control'}),
        'percentage1':forms.TextInput(attrs={'class':'form-control'}),
        'percentage2':forms.TextInput(attrs={'class':'form-control'}),
        'roll_number':forms.TextInput(attrs={'class':'form-control'}),
        'roll_number1':forms.TextInput(attrs={'class':'form-control'}),
        'roll_number2':forms.TextInput(attrs={'class':'form-control'}),
        'course_applied_for':forms.Select(attrs={'class':'form-select'}),
        }
        
class PaymentDetails(forms.ModelForm):
     class Meta:
          model = Payment
          fields = ['user','amount']
          labels = {'user':'UserName', 'amount':'Amount'}
          widgets = {'user':forms.TextInput(attrs={'class':'form-control'}),
                     'amount':forms.TextInput()
          
        }
        
class AdmissionDetails(forms.ModelForm):
     class Meta:
          model = Admission_Status
          fields = ['admission_status']
          labels = {'admission_status':'Admission Status'}
          widgets = {
            'reg_amount': forms.Select(attrs={'class': 'form-select'}),
        }
class AddAdmissionStatus(AdmissionDetails):
      class Meta:
          model = Admission_Status
          fields = ['user', 'reg_amount', 'admission_status']
          widgets = {
            'admission_status': forms.Select(attrs={'class': 'form-select'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
            'reg_amount': forms.Select(attrs={'class': 'form-select'}),
        }

        
       
   
class FeedbackForm(forms.ModelForm):
     class Meta:
          model = Feedback
          fields = ['name','email','message']
          labels = {'name':'Name','email':'Email','message':'Message'}
          widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.TextInput(attrs={'class':'form-control'}),
                'message': forms.Textarea(attrs={'class':'form-control','style':'width=100px','placeholder':'Type Here Some else here..'}),
     }