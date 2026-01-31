from django.contrib import admin
from . models import Addmissionform,Payment,Admission_Status,Feedback,CourseDisplay


@admin.register(CourseDisplay)
class CourseDisplayModelAdmin(admin.ModelAdmin):
    list_display = ['id','image','title','description','course_type']

@admin.register(Addmissionform)
class PersionalModelAdmin(admin.ModelAdmin):
    list_display = ['user','id','firstname','middlename','lastname','fathername','mothername','dob','gender','mobile','email',
   'address','city','state','pin','board','board1','board2','passing_year',"passing_year1",'passing_year2','percentage',
    'percentage1','percentage2','roll_number','roll_number1','roll_number2','photo','signature','matriculation','intermediate','graducation','postgraducation','address_proof','course_applied_for','confirmed']
    readonly_fields = ('created_at','updated_at')

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','payment_date','paymentid','amount_status','display_amount']


@admin.register(Admission_Status)
class AdmissionStatusModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','display_amount','admission_date_time','status_date','admission_status']
    
    fields = (
        'user',
        'reg_amount',
        'admission_date',
        'admission_status',

    )
    readonly_fields = ('admission_date_time','status_date',)

    def admission_date_time(self , obj):
        if obj.admission_date and obj.admission_date.created_at:
            return obj.admission_date.created_at.strftime('%d-%m-%Y %H:%M:%S')
        return "Not Available"
    admission_date_time.short_description = "Admission Date & Time"


                                                                  
@admin.register(Feedback)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','message']

