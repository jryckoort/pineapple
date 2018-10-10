from django.contrib import admin
from .models import Budget, Account, AccountType, CompensationAccount, CompensationAccountCategory, AccountingEntry, ForecastedAccountingEntry

admin.site.register(Budget)
admin.site.register(Account)
admin.site.register(AccountType)
admin.site.register(CompensationAccount)
admin.site.register(CompensationAccountCategory)
admin.site.register(AccountingEntry)
admin.site.register(ForecastedAccountingEntry)
