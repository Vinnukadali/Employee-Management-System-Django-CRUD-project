from django.shortcuts import render,redirect
from .forms import employeeform
from .models import employee

def create_employee(request):
    if request.method == "POST":
        form = employeeform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = employeeform()

    return render(request,"create.html",{'form':form})


def list_employee(request):
    employe = employee.objects.all()
    return render(request,"list.html",{'employee':employe})


def update_employee(request,pk):
    employe = employee.objects.get(id=pk)

    if request.method == "POST":
        form = employeeform(request.POST,instance=employe)

        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = employeeform(instance=employe)

    return render(request,"update.html",{'form':form})


def delete_employee(request,pk):
    employe = employee.objects.get(id=pk)
    employe.delete()
    return redirect('list')