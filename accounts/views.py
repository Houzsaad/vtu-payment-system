from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponse
from .forms import RegisterForm
from wallets.models import Wallet
from transactions.models import Transaction
#from services.models import Services

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.set_transaction_pin(form.cleaned_data['transaction_pin'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

# Create your views here.

def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid email or password.")
    return render(request, 'accounts/login.html')


@login_required
def dashboard(request):
    
    wallet = Wallet.objects.get(user=request.user)

    transactions = Transaction.objects.filter(
        wallet=wallet).order_by('-created_at')[:5]

    context = {
        'wallet': wallet,
        'transactions': transactions
        }
    return render(request, 'accounts/dashboard.html', context)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def logout(request):
    return redirect(login)
