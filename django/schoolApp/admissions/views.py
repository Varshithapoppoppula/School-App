from django.shortcuts import render
from admissions.models import Student
from admissions.models import Teacher
from admissions.forms import StudentModelForm
from admissions.forms import VendorForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
@login_required
def homepage(request):
    return render(request,'index.html')

def logoutUser(request):
    return render(request,'logout.html')

@login_required
def addAdmission(request):
    form=StudentModelForm
    studentform={'form':form}
    if request.method=='POST':
        form=StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)
    return render(request,'admissions/add-Admission.html',studentform)


@login_required
@permission_required('admissions.view_student')
def admissionsReport(request):
    # get all the records from the table
    result=Student.objects.all() # select * from Student
    # store it in dict in Students
    students={'allstudents':result}
    return render(request,'admissions/admissions-Report.html',students)

@login_required
@permission_required('admissions.delete_student')
def deleteStudent(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return admissionsReport(request)

@login_required
@permission_required('admissions.change_student')
def updateStudent(request,id):
    s=Student.objects.get(id=id)
    form=StudentModelForm(instance=s)
    dict={'form':form}
    if request.method=='POST':
        form=StudentModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return admissionsReport(request)
    return render(request,'admissions/update-Admission.html',dict)

@login_required
def addVendor(request):
    form=VendorForm
    vform={'form':form}
    if request.method=='POST':
        form=VendorForm(request.POST)
        if form.is_valid():
            n=form.cleaned_data['name']
            a=form.cleaned_data['address']
            c=form.cleaned_data['contact']
            i=form.cleaned_data['item']
            response=render(request,'index.html');
            request.session['name']=n;
            request.session['address']=a;
            request.session['contact']=c;
            request.session['item']=i;
        return response
    return render(request,'admissions/add-Vendor.html',vform)

class FirstClassBasedView(View):
    def get(self,request):
        return HttpResponse("<h1>This is the First Class Based View</h1>")

class TeacherRead(ListView):
    model=Teacher

class GetTeacher(DetailView):
    model=Teacher

class AddTeacher(CreateView):
    model=Teacher
    fields=('name','exp','subject','contact')

class UpdateTeacher(UpdateView):
    model=Teacher
    fields=('name','exp','subject','contact')

class DeleteTeacher(DeleteView):
    model=Teacher
    success_url=reverse_lazy('listteachers')
