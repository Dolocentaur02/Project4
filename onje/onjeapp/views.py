from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import SignIn
# from .forms import HouseForm, StudentForm


def signIn_list(request):
    signIns = signIn.objects.all()
    return render(request, 'signIn_list.html', {'signIns': signIns})


def signIn_detail(request, id):
    signIn = signIn.objects.get(id=id)
    return render(request, 'signIn_detail.html', {'signIn': signIn})


def signIn_create(response):
    if request.method == 'POST':
        form = signInForm(request.POST)
        if form.is_valid:
            signIn = form.save()
            return redirect('signIn_detail', id=signIn.id)
    else:
        form = signInForm()
        return render(request, 'signIn_form.html', {'form': form})


def signIn_update(request, id):
    signIn = signIn.objects.get(id=id)
    if request.method == 'POST':
        form = signInForm(request.POST, instance=signIn)
        if form.is_valid:
            signIn = form.save()
            return redirect('signIn_detail', id=signIn.id)
    else:
        form = signInForm(instance=signIn)
        return render(request, 'signIn_form.html', {'form': form})


def signIn_delete(request, id):
    if request.method == 'POST':
        signIn.objects.get(id=id).delete()
    return redirect('signIn_list')


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
