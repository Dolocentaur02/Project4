from django import forms
from .models import customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = customer
        fields = ('id', 'name', 'address1', 'address2', 'zip_code', 'city',)


# class StudentForm(forms.ModelForm):

#     class Meta:
#         model = Student
#         fields = ('name', 'image_url', 'house')
