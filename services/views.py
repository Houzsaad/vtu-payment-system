from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from wallets.models import Wallet
from transactions.models import Transaction
from decimal import Decimal

from .forms import ServiceCategory, ServicesPlan, ServiceProvider
from .forms import NetworkSelectionForm, AirtimeForm, DataPlanForm

from .vtpass import purchase_data, purchase_airtime
import uuid
@login_required
def buy_data(request):
    network_form = NetworkSelectionForm(category_slug='data')
    plan_form = None,
    selected_network = None
    
    if request.method == 'POST':
        print('ALL POST KEYS:', list(request.POST.keys()))
        if 'selected_network' in request.POST:
            network_form = NetworkSelectionForm(request.POST, category_slug='data')
            print('Form valid:', network_form.is_valid())
            #print('POST DATA:', request.POST)
          
            print('Form errors:', network_form.errors)
            #print('Form fields:', network_form.fields)
            
            if network_form.is_valid():
                selected_network = network_form.cleaned_data['network']
                plan_form = DataPlanForm(network=selected_network) #data=request.POST

        elif 'select_plan' in request.POST:
            network_id = request.POST.get('network_id')
            selected_network = ServiceProvider.objects.get(id=network_id)
            plan_form = DataPlanForm(network=selected_network, data=request.POST)
            print('Plan Form valid:', plan_form.is_valid())     
            print('Plan Form errors:', plan_form.errors)
                  
            if plan_form.is_valid():
                plan = plan_form.cleaned_data['plan']
                phone = plan_form.cleaned_data['phone']
                request.session['pending_transaction'] = {
                    'plan_id': plan.id,
                    'phone': phone,
                    'amount': str(plan.amount),
                    'service': f"{selected_network.name} {plan.name} Data",
                    'network': selected_network.name
                }
                return redirect('confirm_transaction')
    return render(request, 'services/buy_data.html', {
        'network_form': network_form,
        'plan_form': plan_form,
        'selected_network': selected_network
    })

@login_required 
def buy_airtime(request):   
    network_form = NetworkSelectionForm(category_slug='airtime')
    selected_network = None
    airtime_form = None
    #show_step2 = False

    if request.method == 'POST':
        print('ALL POST KEYS:', list(request.POST.keys()))

        if 'select_network' in request.POST:
            network_form = NetworkSelectionForm(request.POST, category_slug='airtime')
            print('Form valid:', network_form.is_valid())
            print('Form errors:', network_form.errors)
            if network_form.is_valid():
                selected_network = network_form.cleaned_data['network']
                airtime_form = AirtimeForm()
               # print('Selected network:', selected_network)
                #print('Airtime_form:', airtime_form)
         #       show_step2 = True

        elif 'select_airtime' in request.POST:
            network_id = request.POST.get('network_id')
            selected_network = ServiceProvider.objects.get(id=network_id)                
            airtime_form = AirtimeForm(request.POST)
            
            if airtime_form.is_valid():
                phone = airtime_form.cleaned_data['phone']
                amount = airtime_form.cleaned_data['amount']
                request.session['pending_transaction'] = {
                    'phone': phone,
                    'amount': str(amount),
                    'service': f"{selected_network.name} Airtime",
                    'network': selected_network.name,
                    'network_vtpass_id': selected_network.vtpass_services_id
                   
                }
                return redirect('confirm_transaction')
            #else:
            #    show_step2 = True
    return render(request, 'services/buy_airtime.html',{
        'network_form': network_form,
        'airtime_form': airtime_form,
        'selected_network': selected_network,
        #'show_step2': show_step2
    })       
    #return render(request, 'services/buy_airtime.html')

def confirm_transaction(request):
    pending = request.session.get('pending_transaction')

    if not pending:
        return redirect('dashboard')

    if request.method == 'POST':
        pin = request.POST.get('pin')
        #phone = request.POST.get('phone')
        amount = Decimal(pending['amount'])
        #amount = Decimal(request.POST.get('amount'))
        #service = request.POST.get('service')
        user = request.user
        wallet = Wallet.objects.get(user=user)

        if  not user.verify_transaction_pin(pin):
            return render(request, 'services/confirm_transaction.html', {
                    'error': 'incorrect pin',
                    'pending': pending
                    #'phone': phone,
                    #'amount': amount,
                    #'service': service,
                })
        
        try:
            wallet.withdraw(amount)
        except ValueError as e:     
            return render(request, 'services/confirm_transaction.html', {
                'error': str(e),
                'pending': pending
                #'phone': phone,
                #'amount': amount,
                #'service': service,
            })
        # generate unique reference
        reference = uuid.uuid4
        #calling vtpass
        try:
            if 'plan_id' in pending:
                # data purcahe
                plan = ServicesPlan.objects.get(id=pending['plan_id'])
                response = purchase_data(
                    phone_number=pending['phone'],
                    variation_code=plan.vtpass_variation_code,
                    amount=amount,
                    service_id=plan.provider.vtpass_services_id,
                    reference=reference
                )
            else:
                # purcahise airtime
                from .models import ServiceProvider
                network = ServiceProvider.objects.get(vtpass_services_id=pending['network_vtpass_id'])
                response = purchase_airtime(
                    phone_number=pending['phone'],
                    service_id=network.vtpass_services_id,
                    amount=amount,
                    reference=reference
                )
            print('Vtpass response:', response)
            # response status
            if response.get('code') == '000':
                status = Transaction.TransactionStatus.COMPLETED
            else:
                #refund the money
                wallet.deposit(amount)
                status = Transaction.TransactionStatus.FAILED
        
        except Exception as e:
            # refund wallet if api fails
            wallet.deposit(amount)
            status = Transaction.TransactionStatus.FAILED
            print('Vtpass error:', e)

            #log trxns
        Transaction.objects.create(
            wallet=wallet,  
           # transantion_type=Transaction.TransactionType.VTU_PURCHASE,
            user=user,
            phone_number=pending['phone'],
            amount=amount,
            status=status,
            #description=f"{pending['service']} for {pending['phone']}"
        )
        del request.session['pending_transaction']
        if status == Transaction.TransactionStatus.COMPLETED:
            return redirect('dashboard')
        else:
            return render(request, 'services/confirm_transaction.html', {
                'error': 'Transaction failed. Your wallet has been refunded',
                'pending': pending
            })


    return render(request, 'services/confirm_transaction.html')