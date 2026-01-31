
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.utils import timezone  
from  account.models import User

#Home Page Model
COURSE_TYPE = [
    ('premium','Premium'),
    ('sort_term','Sort_Term'),
    ('professional','Professional'),
    ('free','Free'),
]

class CourseDisplay(models.Model):
    image=models.ImageField(upload_to='course_image',blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    what_you_will_learn = models.TextField(blank=True)
    course_price = models.DecimalField(max_digits=8,decimal_places=2,null=True, blank=True,default=400.00)
    course_duration = models.CharField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course_type = models.CharField(max_length=15,choices=COURSE_TYPE,default='premium')
  



# Create your models here




STATE_CHOICE=(
    ('Andman & Nicobar Island','Andman & Nicobar Island',),
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujrat','Gujrat'),
    ('Haryana','Hryana'),
    ('Himachal Pradesh','Himachal Pradesh'),
    ('Jammu & Kasmir','Jammu & Kasmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerla','Kerla'),
    ('Lakshadweep','Lakshadweep'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalay','Meghalay'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajsthan','Rajsthan'),
    ('Sikkim','Sikkim'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Telangana','Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),

)


COURSE_CHOICE=(
 ('6th','6th'),
 ('7th','7th'),
 ('8th','8th'),
 ('9th','9th'),
 ('10th,','10th'),
 ('11th','11th'),
 ('12th','12th'),
 ('Graduation','Graduation'),
 ('Special Classes','Special Clases'),
 ('DCA','DCA'),
 ('CFA','CFA'),
 ('DDTP','DDTP'),
 ('DCAD','DCAD'),
 ('ADCA','ADCA'),
 ('DCP','DCP'),
 ('HDCA','HDCA'),
 ('DAP','DAP'),
 ('HDAP','HDAP'),
 ('HDIT','HDIT'),
 ('ADIT','ADIT'),
 ('DCH','DCH'),
 ('ADCHN','ADCHN'),
 ('DCN','DWD'),
 ('DWD','DWD'),
 ('DMM','DMM'),
 ('ADGA','ADGA'),
 ('DCT','DCT'),
 ('DOM','DOM'),
 ('DMR','DMR'),
 ('DID','DID'),
 ('Professional Courses','Professional Courses',)
)

class Addmissionform(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname =  models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    dob        = models.DateField(auto_now = False, auto_now_add = False)
    gender     = models.CharField(max_length=100)
    mobile     = models.PositiveIntegerField()
    email      = models.EmailField()
    address    = models.CharField(max_length=150)
    city       = models.CharField(max_length=100)
    state      = models.CharField(choices= STATE_CHOICE,  max_length=25)
    pin        = models.PositiveIntegerField()
    board=models.CharField(max_length=100,blank=True,null=True)
    board1=models.CharField(max_length=100,blank=True,null=True)
    board2=models.CharField(max_length=100,blank=True,null=True)
    passing_year=models.PositiveBigIntegerField(blank=True,null=True)
    passing_year1=models.PositiveBigIntegerField(blank=True,null=True)
    passing_year2=models.PositiveBigIntegerField(blank=True,null=True)
    percentage=models.CharField(max_length=100,blank=True,null=True)
    percentage1=models.CharField(max_length=100,blank=True,null=True)
    percentage2=models.CharField(max_length=100,blank=True,null=True)
    roll_number=models.PositiveBigIntegerField(blank=True,null=True) 
    roll_number1=models.PositiveBigIntegerField(blank=True,null=True)
    roll_number2=models.PositiveBigIntegerField(blank=True,null=True)
    photo=models.ImageField(upload_to='photoimage',blank=True)
    signature=models.ImageField(upload_to='signatureimage',blank=True)
    matriculation=models.FileField(upload_to='matricdoc',blank=True)
    intermediate=models.FileField(upload_to='intermediatedoc',blank=True)
    graducation=models.FileField(upload_to='graducationdoc',blank=True)
    postgraducation=models.FileField(upload_to='postgraducationdoc',blank=True)
    address_proof=models.FileField(upload_to='photodoc',blank=True)
    course_applied_for=models.CharField(choices=COURSE_CHOICE,max_length=25)
    price = models.ForeignKey(CourseDisplay,on_delete=models.CASCADE,null=True,blank=True)
    registration_number = models.CharField(max_length=20,unique=True,null=True)
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}-{self.created_at.strftime('%d-%m-%Y %H:%M:%S')}"

    def save(self,*args,**kwargs):
        if not self.registration_number:
            last_id = Addmissionform.objects.all().count()+1
            self.registration_number = f"SV{timezone.now().year}{last_id:04d}"
        super().save(*args, **kwargs)
           
    
    # def __str__(self):
    #     return self.user
  
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(max_length=100,unique=True)
    signature = models.CharField(max_length=200,blank=True,null=True)
    paymentid = models.CharField(max_length=100,blank=True,null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}-{self.amount/100} INR - {'Paid' if self.paid else 'Pending'}"
    @property
    def amount_status(self):
        return f"{'Success' if self.paid else 'Fail'}"
        
    @property
    def display_amount(self):
        return self.amount / 100
   
STATUS_CHOICE=(
    ('Payment_Not_Completed','Payment_Not_completed'),
    ('Accepted','Accepted'),
    ('Succsess','Succsess'),
    ('Cancel','Cancel'),
)
class Admission_Status(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reg_amount = models.ForeignKey(Payment,on_delete=models.CASCADE)
    admission_date = models.ForeignKey(Addmissionform, on_delete=models.SET_NULL, null=True, blank=True)
    status_date =models.DateTimeField(auto_now=True)
    admission_status = models.CharField(max_length=50,choices=STATUS_CHOICE,default='Pending')


    @property
    def display_amount(self):
        return self.reg_amount.amount / 100
    @property
    def admission_date_time(self):
        return self.admission_date.created_at
  
class Feedback(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    message=models.CharField(max_length=200)