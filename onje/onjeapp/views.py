from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import customer
from .forms import CustomerForm


def customer_list(request):
    customers = customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})


def customer_detail(request, id):
    customer = customer.objects.get(id=id)
    return render(request, 'customer_detail.html', {'customer': customer})


def customer_create(response):
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid:
            customer = form.save()
            return redirect('customer_detail', id=customer.id)  
    else:
        form = customerForm()
        return render(request, 'customer_form.html', {'form': form})


def customer_update(request, id):
    customer = customer.objects.get(id=id)
    if request.method == 'POST':
        form = customerForm(request.POST, instance=customer)
        if form.is_valid:
            customer = form.save()
            return redirect('customer_detail', id=customer.id)
    else:
        form = customerForm(instance=customer)
        return render(request, 'customer_form.html', {'form': form})


def customer_delete(request, id):
    if request.method == 'POST':
        customer.objects.get(id=id).delete()
    return redirect('customer_list')


# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'student_list.html', {'students': students})


# def student_detail(request, id):
#     student = Student.objects.get(id=id)
#     return render(request, 'student_detail.html', {'student': student})


# def student_create(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid:
#             student = form.save()
#             return redirect('student_detail', id=student.id)
#     else:
#         form = StudentForm()
#         return render(request, 'student_form.html', {'form': form})


# def student_update(request, id):
#     student = Student.objects.get(id=id)
#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid:
#             student = form.save()
#             return redirect('student_detail', id=student.id)
#     else:
#         form = StudentForm(instance=student)
#         return render(request, 'student_form.html', {'form': form})


# def student_delete(request, id):
#     if request.method == 'POST':
#         Student.objects.get(id=id).delete()
#     return redirect('student_list')
