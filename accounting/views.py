from django.shortcuts import render
from .models import Account

def index(request):
    accounts = Account.objects.order_by('name')
    return render(request, 'accounting/index.html', {'accounts': accounts})
