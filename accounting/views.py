from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Account, Budget, AccountingEntry, PlannedAccountingEntry
from .forms import AccountingEntryForm

#Accounts view
def accounts(request, id_budget):
    accounts = Account.objects.filter(budget=id_budget)
    return render(request, 'accounting/index_accounts.html', locals())

#Operations view
def operations(request, id_budget):
    #Budget
    budget = Budget.objects.get(id=id_budget)

    #Récupération des dernières opérations
    entries = AccountingEntry.objects.filter(account__budget=id_budget).order_by('-date')

    return render(request, 'accounting/index_operations.html', locals())

#Operations view
def planned_operations(request, id_budget):
    #Budget
    budget = Budget.objects.get(id=id_budget)

    #Récupération des opérations à venir
    next_entries = PlannedAccountingEntry.objects.filter(account__budget=id_budget).order_by('date')

    return render(request, 'accounting/index_operations.html', locals())


def add_operation(request):

    form = AccountingEntryForm(request.POST or None)
    if form.is_valid():
        form.save()

        #Effectuer la comptabilité !

        add = True
        return redirect('operations', id_budget='1')
    else:
        return render(request, 'accounting/add_operation.html', locals())

def view_operation(request, id_operation):
    entry = AccountingEntry.objects.get(id=id_operation)

    return render(request, 'accounting/view_operation.html', locals())
