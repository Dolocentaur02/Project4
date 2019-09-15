
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact, Product
from .forms import ContactForm, ProductForm, ContactUsForm

def emailView(request):
    if request.method == 'GET':
        form = ContactUsForm()
    else:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


def contact_detail(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'contact_detail.html', {'contact': contact})


def contact_create(response):
    if response.method == 'POST':
        form = ContactForm(response.POST)
        if form.is_valid:
            contact = form.save()
            return redirect('contact_detail', id=contact.id)  
    else:
        form = ContactForm()
        return render(response, 'contact_form.html', {'form': form})


def contact_update(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid:
            contact = form.save()
            return redirect('contact_detail', id=contact.id)
    else:
        form = ContactForm(instance=contact)
        return render(request, 'contact_form.html', {'form': form})


def contact_delete(request, id):
    if request.method == 'POST':
        Contact.objects.get(id=id).delete()
    return redirect('contact_list')

def Product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html')


def Product_detail(request, id):
    Product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product':product})


def Product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid:
            Product = form.save()
            return redirect('product_detail', id=product.id)
    else:
        form = ProductForm()
        return render(request, 'product_form.html', {'form': form})


def Product_update(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=Product)
        if form.is_valid:
            Product = form.save()
            return redirect('product_detail', id=Product.id)
    else:
        form = ProductForm(instance=Product)
        return render(request, 'product_form.html', {'form': form})


def Product_delete(request, id):
    if request.method == 'POST':
        Product.objects.get(id=id).delete()
    return redirect('product_list')
