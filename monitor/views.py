from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .forms import SignupForm, CredentialForm
from .models import Credential
from django.contrib.auth.decorators import login_required
from .utils import check_leakcheck

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    credentials = Credential.objects.filter(user=request.user)
    breach_errors = {}
    for credential in credentials:
        is_breached, breach_details = check_leakcheck(credential.email)
        if is_breached is not None:
            credential.is_breached = is_breached
            credential.breach_details = breach_details if is_breached else []
            credential.save()
        else:
            breach_errors[credential.email] = breach_details
    return render(request, 'dashboard.html', {
        'user': request.user,
        'credentials': credentials,
        'breach_errors': breach_errors,
    })

@login_required
def add_credential(request):
    if request.method == 'POST':
        form = CredentialForm(request.POST)
        if form.is_valid():
            try:
                credential = form.save(commit=False)
                credential.user = request.user
                credential.save()
                return redirect('dashboard')
            except IntegrityError:
                form.add_error('email', 'This email is already being monitored.')
    else:
        form = CredentialForm()
    return render(request, 'add_credential.html', {'form': form})

@login_required
def delete_credential(request, pk):
    credential = get_object_or_404(Credential, pk=pk, user=request.user)
    if request.method == 'POST':
        credential.delete()
    return redirect('dashboard')

@login_required
def check_credential(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        is_breached, result = check_leakcheck(email)
        return render(request, 'check_result.html', {
            'email': email,
            'is_breached': is_breached,
            'breaches': result if isinstance(result, list) else None,
            'error': result if isinstance(result, str) else None
        })
    return render(request, 'check_credential.html')
