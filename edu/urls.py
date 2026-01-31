from django.urls import path
from  edu import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Home,name='home1' ),
    path('coursedetail/view/<int:id>/',views.CourseDetail,name='course_detail'),
    path('about',views.about1,name='about1' ),
    path('course',views.course,name='course' ),
    path('feedback',views.feedback,name='feedback' ),
    path('changepass/',views.user_change_pass,name='changepass'),
    path('logout/',views.user_logout, name='logoutedu'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('admissionform/',views.admission_details, name='admissiondetails'),
    path('formpreview/<int:pk>/',views.AdmissionPreview,name='formpreview'),
    path("admission/edit/<int:pk>/", views.AdmissionEdit, name="admission_edit"),
    path('payment/',views.payment_details, name='payment'),
    # path('educationaldetails',views.education_details, name='educationaldetails'),
    # path('uploaddocument',views.upload_document, name='uploaddocument'),
    # path('feedetails',views.fee_details, name='feedetails'),
    path('printform/',views.Admission_Details, name='printform'),
    path('admissionstatus/',views.Admission_status, name='admissionstatus'),
    path('success/',views.success_payment, name="success"),
    path('payri/',views.payment_print,name="payri")
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

