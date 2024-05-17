from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .forms import RegisterForm, CustomerForm
from .models import Customer


app_name = 'my_app'


def home(request):
    customers = Customer.objects.all().order_by('last_name')
    context = {'customers': customers}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('my_app:home')
        else:
            messages.success(request, 'Invalid login credentials')
            return redirect('my_app:home')
    return render(request, 'my_app/home.html', context)

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('my_app:home')


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created for ' + username)
            return redirect('my_app:home')
    else:
        form = RegisterForm()
        return render(request, 'my_app/register.html', {'form': form})

    return render(request, 'my_app/register.html', {'form': form})


def customer_detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    return render(request, 'my_app/customer_detail.html', {'customer': customer})

def delete_customer(request, customer_id):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=customer_id)
        customer.delete()
        messages.success(request, 'Customer has been deleted')
        return redirect('my_app:home')
    else:
        messages.success(request, 'Your not authorized to delete this customer')
    return redirect('my_app:home')

def add_customer(request):
    form = CustomerForm(request.POST)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Customer has been added')
                return redirect('my_app:home')
        else:
            form = CustomerForm()
            return render(request, 'my_app/add_customer.html', {'form': form})
    else:
        messages.success(request, 'Your not authorized to add a customer')
        return redirect('my_app:home')

    return render(request, 'my_app/add_customer.html', {'form': form})


def update_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    form = CustomerForm(request.POST or None, instance=customer)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Customer has been updated')
                return redirect('my_app:home')
        else:
            form = CustomerForm(instance=customer)
            return render(request, 'my_app/update_customer.html', {'form': form})
    else:
        messages.success(request, 'Your not authorized to update this customer')
        return redirect('my_app:home')

    return render(request, 'my_app/update_customer.html', {'form': form})

#search customers by name city adress using ajax

def search_customer(request):
    if request.method == 'POST':
        search = request.POST.get('search_customer', None)
        print('search', search )

        if search is not None:
            customers = Customer.objects.filter(first_name__icontains=search) | Customer.objects.filter(last_name__icontains=search) | Customer.objects.filter(city__icontains=search)
            print('customers', customers)
             # Sérialiser les objets
            customer_list = list(customers.values('id', 'first_name', 'last_name', 'city'))
            print('customer_list', customer_list)
            return JsonResponse(customer_list, safe=False)
    else:
        return render(request, 'my_app/home.html')


