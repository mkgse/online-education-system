from django.contrib import admin
from . models import Addmissionform,Payment,Admission_Status,Feedback

@admin.register(Addmissionform)
class PersionalModelAdmin(admin.ModelAdmin):
    list_display = ['user','id','firstname','middlename','lastname','fathername','mothername','dob','gender','mobile','email',
   'address','city','state','pin','board','board1','board2','passing_year',"passing_year1",'passing_year2','percentage',
    'percentage1','percentage2','roll_number','roll_number1','roll_number2','photo','signature','matriculation','intermediate','graducation','postgraducation','address_proof','course_applied_for']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','payment_date','paymentid','amount_status','display_amount']


@admin.register(Admission_Status)
class AdmissionStatusModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','display_amount','admissin_date','admission_status']
                                                                  
@admin.register(Feedback)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message']

