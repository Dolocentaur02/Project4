
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact, Product
from .forms import ContactForm, ProductForm, ContactUsForm, LoginForm
from django.contrib.auth.decorators import login_required


def emailView(request):
    if request.method == 'GET':
        form = ContactUsForm()
    else:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            return redirect('success')
    return render(request, "email.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')

@login_required
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


@login_required
def contact_detail(request, id):
    contact = Contact.objects.get(id=id)
    return render(request, 'contact_detail.html', {'contact': contact})


def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            contact = form.save()
            return redirect('contact_detail', id=contact.id)
    else:
        form = ContactForm()
        return render(request, 'contact_form.html', {'form': form})

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

@login_required
def Product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'product': products})

@login_required
def Product_detail(request, id):
    Product = Product.objects.get(id=id)
    return render(request, 'product_detail.html', {'product': Product})


@login_required
def Product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid:
            Product = form.save()
            return redirect('product_detail', id=Product.id)
    else:
        form = ProductForm()
        return render(request, 'product_form.html', {'form': form})


@login_required
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


@login_required
def Product_delete(request, id):
    if request.method == 'POST':
        Product.objects.get(id=id).delete()
    return redirect('product_list')


def pagelogin(request):

    uservalue = ''
    passwordvalue = ''

    form = LoginForm(request.POST or None)
    if form.is_valid():
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context = {'form': form,
                       'error': 'The login has been successful'}
            return render(request, 'siteusers/login.html', context)
        else:
            context = {'form': form,
                       'error': 'The username and password combination is incorrect'}
            return render(request, 'siteusers/login.html', context)

    else:
        context = {'form': form}
        return render(request, 'siteusers/login.html', context)
@login_required
def searchproducts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Product(title=query) | Product(description=query)

            products= Product.objects.filter(lookups).distinct()

            context={'product': Product,
                     'submitbutton': submitbutton}

            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')

    else:
        return render(request, 'search.html')
