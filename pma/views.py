import json
from django.contrib import auth, messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Usage

def home(request):
    """
    Render the home page.
    """
    return render(request, 'home.html')

def user_actions(request):
    """
    Handle user actions from the home page form.
    """
    if request.method == 'POST':
        action = request.POST.get('action', '')

        if action == 'logout':
            logout(request)
            return redirect('home')
        elif action == 'view_data':
            return redirect('d3_graph')
        elif action in ['login', 'register']:
            return redirect(action)

    # Handle the case where the form is not submitted or the action is not recognized
    return render(request, 'home.html')

def register(request):
    """
    Handle user registration.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
                messages.info(request, 'Email or Username already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    """
    Handle user login.
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('user_login')
    else:
        return render(request, 'login.html')

@csrf_exempt
def get_property_data(request, property_id, meter_type):
    """
    Retrieve property data for a specific property and meter type.
    """
    if request.method == 'POST':
        try:
            usage_objects = Usage.objects.filter(property_id=property_id, meter_type=meter_type)
            data = [{'date': obj.date.split()[0], 'value': obj.common_usage_units} for obj in usage_objects]

            return JsonResponse(data, safe=False)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_meter_types(request, property_id):
    """
    Retrieve meter types for a specific property.
    """
    if request.method == 'GET':
        try:
            meter_types = Usage.objects.filter(property_id=property_id).values_list('meter_type', flat=True).distinct()
            return JsonResponse({'meter_types': list(meter_types)})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@login_required(login_url='login')
def d3_graph(request):
    """
    Render the D3 graph page with property data.
    """
    # Retrieve data from the database
    usageDetails = Usage()

    # Get all unique property_ids
    property_ids = Usage.objects.values_list('property_id', flat=True).distinct()

    # You can now use property_data in your view
    return render(request, 'd3-graph.html', {'property_ids': property_ids})