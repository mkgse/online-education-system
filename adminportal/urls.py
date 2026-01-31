from django.urls import path
from  .import views

urlpatterns = [
      #course CRUD
    path('course/detail/',views.course_detail,name='course_detail'),
    path('update_course/<int:id>/',views.update_course,name='update_course'),
    path('view_course/<int:id>/',views.view_course,name='view_course'),
    path('add_course/',views.add_course,name='add_course'),
    path('delete/course/<int:id>',views.delete_course,name='delete_course'),
    path('login/',views.admin_login,name='adminlogin' ),
    path('admindashboard/',views.admin_dashboard , name="admindashboard"),
    path('delete/<int:id>/',views.delete_form , name='deleteform'),
    path('viewform/<int:id>/',views.view_form , name='viewform'),
    path('<int:id>/',views.update_form , name='updateform'),
    path('AdmissionStatus/Add/',views.Add_Admissionstatus , name='AdmissionStatus'),
    path('studadmistatus/',views.admission_status , name='admstatus'),
    path('status/<int:id>/',views.update_status , name='updatestatus'),
    path('deletestatus/<int:id>/',views.delete_status , name='deletestatus'),
    path('studentpaymentdetails/',views.student_payment_details,name='studentpaymentdetails'),
    path('feedbackdetails/',views.feedback_details,name='feedbackdetails'),
    path('logout/',views.logout_view,name='logout'),

 
]

