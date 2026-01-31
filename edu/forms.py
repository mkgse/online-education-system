from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm  
from django.utils.translation import gettext, gettext_lazy as _ 
from .models import Addmissionform,Payment,Admission_Status,Feedback,CourseDisplay
from datetime import datetime,date
from account.models import User


#Cousre Form

class CourseDisplayForm(forms.ModelForm):
     class Meta:
          model = CourseDisplay
          fields = ['image','title','description','what_you_will_learn','course_price','course_duration','course_type']
          widgets = {
               'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'what_you_will_learn':forms.Textarea(attrs={'class':'form-control'}),
            'course_price':forms.TextInput(attrs={'class':'form-control'}),
            'course_duration':forms.TextInput(attrs={'class':'form-control'}),
            'course_type': forms.Select(attrs={'class': 'form-select'}),

          }



GENDER_CHOICES=[
     ('Male','Male'),
     ('Female','Female')
]

        
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
        'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker', 'type': 'date'}),
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
        'photo': forms.FileInput(),
        'signature': forms.FileInput(),
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
          fields = '__all__'
          exclude = ['status_date']
          widgets = {
            'admission_status': forms.Select(attrs={'class': 'form-select'}),
            'admission_date': forms.Select(attrs={'class':'form-select'}),
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
                'message': forms.Textarea(attrs={'class':'form-control','style':'width=50px;height=80px','placeholder':'Type Here Some else here..'}),
     }