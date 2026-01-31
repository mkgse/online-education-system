from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages,auth
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.urls import reverse
from django.contrib import auth
from account.models import User
from edu.forms import SignUpForm, LoginForm


# Create your views here.
# ------------------- AUTH -------------------
def admission(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('admissiondetails')
        else:
            messages.error(request,'Invalid login credentials or Your account is not active')
            return redirect('admission')
        
    else:
        form = LoginForm()
    return render(request, 'account/admission.html', {'form': form})


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            username = email.split("@")[0]

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user.phone_number = phone_number
            user.save()

            # USER ACTIVATION EMAIL
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'

            mail_message = render_to_string(
                'account/account_verification_email.html',
                {
                    'user': user,
                    'domain': current_site,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                }
            )

            send_email = EmailMessage(
                mail_subject,
                mail_message,
                to=[email]
            )
            send_email.send()

            messages.success(
                request,
                'Please check your email to activate your account'
            )
            return redirect('admission')
    else:
        form = SignUpForm()

    return render(request, 'account/signup.html', {'form': form})


def activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        messages.success(request,'Congratulations! Your account is activated.')
        return redirect('admission')
    else:
        messages.error(request,'Invalid activation link')
        return redirect('signup')

def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email__exact = email)
            #Reset Password Email
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('account/reset_password_email.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),     

            })
            to_email = email
            send_email = EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()
            messages.success(request,'Password reset email has been sent to your email address.')
            return redirect('admission')
        else:
            messages.error(request,'Account does not exist!')
            return redirect('forgotPassword')
    return render(request,'account/forgotPassword.html') 

def resetpassword_validate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid'] = uid
        return redirect('resetPassword')
    else:
        messages.error(request,'This link has been expired!')
        return redirect('admission')

def resetPassword(request):
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = User.objects.get(pk=uid)
            user = User.objects.get(pk = uid)
            user.set_password(password)
            user.save()
            messages.success(request,'Password reset successful')
            return redirect('admission')
        else:
            messages.error(request,'Password do not match!')
            return redirect('resetPassword')
    else:
        return render(request,'account/resetPassword.html')
