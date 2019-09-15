from django import forms
from .models import Contact, Product


class ContactForm(forms.ModelForm):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        model = Contact
        fields = ('name',)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'image_url',)


class ContactUsForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
