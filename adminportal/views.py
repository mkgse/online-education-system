from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from edu.forms import LoginForm, AdmDetails, AdmissionDetails,AddAdmissionStatus
from edu.models import Addmissionform, Admission_Status, Payment, Feedback
from django.urls import reverse
from django.core.paginator import Paginator

# ----------------------------Admin Login------------------------

def admin_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None and user.is_superuser:
                    login(request, user)
                    messages.success(request, 'Congratulations!! You have successfully logged in.')
                    return HttpResponseRedirect('/adminn/admindashboard/')
                else:
                    messages.info(request, 'You are not an Admin or credentials are invalid!')
        else:
            form = LoginForm()
        return render(request, 'adminportal/admin_login.html', {'form': form})
    else:
        return HttpResponseRedirect('/edu/dashboard')
        
        # ---------------------------------Admission List-------------------------
def admin_dashboard(request):
    admission_list = Addmissionform.objects.all().order_by("-registration_number")
    paginator = Paginator(admission_list,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'adminportal/admindashboard.html', {'admission_list': page_obj})


def delete_form(request, id):
    if request.method == 'POST':
        pi = get_object_or_404(Addmissionform, pk=id)
        pi.delete()
        return HttpResponseRedirect(reverse('admindashboard'))

def view_form(request, id):
        form = get_object_or_404(Addmissionform, pk=id)
        print(form)
        return render(request, 'adminportal/viewform.html', {'fm': form})

def update_form(request, id):
    pi = get_object_or_404(Addmissionform, pk=id)
    if request.method == 'POST':
        fm = AdmDetails(request.POST,request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your data has been successfully modified!')
            return HttpResponseRedirect(reverse('admindashboard'))
    else:
        fm = AdmDetails(instance=pi)
    return render(request, 'adminportal/updateform.html', {'details': fm})

#  -------------------------Admission Status----------------------------------
def Add_Admissionstatus(request):
    if request.method == 'POST':
        form = AddAdmissionStatus(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Admission created successfully!')
            return redirect('admstatus')
    else:
        form = AddAdmissionStatus()
    return render(request,'adminportal/AddAdmissionStatus.html',{'form':form})
       
def admission_status(request):
    form = Admission_Status.objects.select_related('user', 'reg_amount').all()
    paginator = Paginator(form,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'adminportal/admstatus.html', {'form': page_obj})
    

def update_status(request, id):
    pt = get_object_or_404(Admission_Status, pk=id)
    if request.method == 'POST':
        fm = AdmissionDetails(request.POST, instance=pt)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Admission updated successfully!')
            return HttpResponseRedirect(reverse('admstatus'))
    else:
        fm = AdmissionDetails(instance=pt)
    return render(request, 'adminportal/updateadmissionstatus.html', {'form': fm, 'student': pt})

def delete_status(request, id):
    pi = get_object_or_404(Admission_Status, pk=id)
    if request.method == 'POST':
        pi.delete()
        return HttpResponseRedirect(reverse('admstatus'))
 

# ----------------------------Student Payment Status Admin View-----------------------
def student_payment_details(request):
    status = request.GET.get("status") 
    form = Payment.objects.all().order_by('-payment_date')

    if status == "success":
        form = form.filter(paid=True)
    elif status == "failed":
        form = form.filter(paid=False)
    paginator = Paginator(form,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'adminportal/studentpayment.html', {'page_obj': page_obj,'status':status})
# -----------------------------Student FeedBack Admin View------------------------
def feedback_details(request):
    form = Feedback.objects.all()  
    paginator = Paginator(form,10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)        
    return render(request, 'adminportal/feedbackdetails.html', {'form': page_obj})
# -----------------------------Logout Admin View-----------------
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/adminn/login/')
