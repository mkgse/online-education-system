from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
import razorpay
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.http import HttpResponseBadRequest
from .forms import (
    SignUpForm, LoginForm, ChangeForm, AdmDetails,
    PaymentDetails, FeedbackForm
)
from .models import Payment, Addmissionform, Admission_Status, Feedback,CourseDisplay

import razorpay
from datetime import date, datetime



# ------------------- HOME -------------------
def Home(request):
    if not request.user.is_authenticated:
           sort_by = request.GET.get('sort','all')
           if sort_by == 'premium':
              courses = CourseDisplay.objects.filter(course_type = 'premium')
           elif sort_by == 'sort_term':
                courses = CourseDisplay.objects.filter(course_type = 'sort_term')
           elif sort_by == 'professional':
                courses = CourseDisplay.objects.filter(course_type = 'professional')
           elif sort_by == 'free':
                courses = CourseDisplay.objects.filter(course_type = 'free')
           else:
                 courses = CourseDisplay.objects.all()
           return render(request, 'edu/Index.html',{'course_details':courses})
    user = request.user
    sort_by = request.GET.get('sort','all')
    if sort_by == 'premium':
         courses = CourseDisplay.objects.filter(course_type = 'premium')
    elif sort_by == 'sort_term':
         courses = CourseDisplay.objects.filter(course_type = 'sort_term')
    elif sort_by == 'professional':
            courses = CourseDisplay.objects.filter(course_type = 'professional')
    elif sort_by == 'free':
         courses = CourseDisplay.objects.filter(course_type = 'free')
    else:
         courses = CourseDisplay.objects.all()
    return render(request, 'edu/Index.html', {'course_details':courses,'full_name': user.full_name()})

def CourseDetail(request,id):
    courses = get_object_or_404(CourseDisplay,id=id)
    print(courses)
    return render(request, 'edu/coursedetails.html',{'course_details':courses})


def about1(request):
    return render(request, 'edu/about1.html')


def course(request):
    return render(request, 'edu/course.html')

def user_change_pass(request):
    if not request.user.is_authenticated:
        return redirect('admission')

    if request.method == "POST":
        form = ChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been successfully changed!')
            return redirect("admission")
    else:
        form = ChangeForm(user=request.user)

    return render(request, 'edu/changepass.html', {
        'form': form,
        'full_name': request.user.full_name()
    })


def user_logout(request):
    logout(request)
    return redirect('admission')
# ----------------------------Dashboard-------------------------
def dashboard(request):
    return render(request,'edu/dashboard.html')

# ------------------- ADMISSION FORM -------------------

def admission_details(request):
    if not request.user.is_authenticated:
        return redirect('admission')

    draft = Addmissionform.objects.filter(user=request.user,confirmed = False).last()
    if draft:
         return redirect("formpreview", pk=draft.pk)

    if request.method == "POST":
        details = AdmDetails(request.POST, request.FILES)
        if details.is_valid():
            obj = details.save(commit=False)
            obj.user = request.user
            obj.confirmed = False   # mark as draft
            obj.save()
            return redirect("formpreview", pk=obj.pk)  # pass record ID
    else:
        details = AdmDetails()
        form = Addmissionform.objects.filter(user=request.user)

    return render(request, 'edu/admissionform.html', {
        'details': details,
        'full_name': request.user.full_name(),
        'user': request.user.username,
        'form':form
    })


def AdmissionPreview(request, pk):
    if not request.user.is_authenticated:
        return redirect("admission")  # force login first

    obj = get_object_or_404(Addmissionform, pk=pk, user=request.user)

    if request.method == "POST":
        if "confirm" in request.POST:
            obj.confirmed = True
            obj.save()
            return redirect("payment")  # after confirm
        elif "edit" in request.POST:
            return redirect("admissiondetails")  # edit existing record
    context = {
        'data':obj,
        'full_name': request.user.full_name(),
    }

    return render(request, "edu/admission_preview.html",context)



def AdmissionEdit(request, pk):
    obj = get_object_or_404(Addmissionform, pk=pk, user=request.user)

    if request.method == "POST":
        form = AdmDetails(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("formpreview", pk=obj.pk)  # back to preview after edit
    else:
        form = AdmDetails(instance=obj)
        context = {
          "form": form,
          "full_name": request.user.full_name(),
        }

    return render(request, "edu/admission_edit.html", context)


    


def Admission_Details(request):
    if not request.user.is_authenticated:
        return redirect('admission')

    form = Addmissionform.objects.filter(user=request.user)
    return render(request, 'edu/preview.html', {
        'full_name': request.user.full_name(),
        'form': form
    })



def Admission_status(request):
    admstatus = Admission_Status.objects.filter(user=request.user)
    return render(request, 'edu/admissionstatus.html', {'admstatus': admstatus,'full_name': request.user.full_name()})

# ------------------- PAYMENT -------------------
def payment_details(request):
    if not request.user.is_authenticated:
        return redirect('admission')

    if request.method == 'POST':
        amount = request.POST.get("amount")
        if not amount:
            return render(request,'edu/payment.html',{'error':'Amount is required'})
        
        amount = int(amount) * 100 #paise
        client = razorpay.Client(auth=("rzp_test_ugBbbb0MY8YfMB","KSFeqtlQkQFJ1kCblDsUzPGF"))
        order = client.order.create(dict(amount=amount, currency="INR", payment_capture="1"))
        Payment.objects.create(user=request.user, amount=amount, order_id=order['id'],paid=False)
        return render(request, 'edu/payment.html', {'payment': Payment,'order':order,})

    return render(request, 'edu/payment.html',{'payment':None,'full_name': request.user.full_name()})


@csrf_exempt
def success_payment(request):
    # Handle Razorpay succes call Back
    if request.method == "POST":
        params_dict = {
            'razorpay_order_id': request.POST.get('razorpay_order_id'),
            'razorpay_payment_id': request.POST.get('razorpay_payment_id'),
            'razorpay_signature': request.POST.get('razorpay_signature')
        }
        client = razorpay.Client(auth=("rzp_test_ugBbbb0MY8YfMB","KSFeqtlQkQFJ1kCblDsUzPGF"))

        try:
            # Verify the payment signature
           client.utility.verify_payment_signature(params_dict)
        except razorpay.errors.SignatureVerificationError:
            return HttpResponseBadRequest("Payment verification failed!")
         # Mark Payment as Successfull

        payment = Payment.objects.get(order_id = params_dict['razorpay_order_id'])
        payment.paymentid = params_dict['razorpay_payment_id']
        payment.signature = params_dict['razorpay_signature']
        payment.paid = True
        payment.save()
      
        return render(request, 'edu/paymentsucsess.html',{'payment':payment,})

    return HttpResponseBadRequest("Invalid request")


def payment_print(request):
    return render(request, "edu/paymentprintreciept.html")


# ------------------- FEEDBACK -------------------
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create(**form.cleaned_data)
            messages.success(request, 'Your feedback has been submitted successfully!')
            form = FeedbackForm()
    else:
        form = FeedbackForm()
    return render(request, 'edu/feedback.html', {'form': form})
