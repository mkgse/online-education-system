from django.urls import path
from  account import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admission',views.admission,name='admission'),
    path('signup/',views.sign_up,name='signup'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
    path('resetpassword_validate/<uidb64>/<token>',views.resetpassword_validate, name='resetpassword_validate'),
    path('forgotPassword/',views.forgotPassword,name='forgotPassword'),
    path('resetPassword/',views.resetPassword,name='resetPassword'),
  
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

