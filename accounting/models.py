from django.db import models

class Budget(models.Model):
    user = models.ManyToManyField('auth.User')
    name = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Account(models.Model):
    budget = models.ForeignKey('Budget', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.TextField()
    balance = models.DecimalField(max_digits=13, decimal_places=2)
    type = models.ForeignKey('AccountType', on_delete=models.PROTECT)

    class Meta:
        ordering = ('budget','type',)

    def __str__(self):
        return self.name

class AccountType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class CompensationAccount(models.Model):
    budget = models.ForeignKey('Budget', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.TextField()
    balance = models.DecimalField(max_digits=13, decimal_places=2)
    category = models.ForeignKey('CompensationAccountCategory', on_delete=models.PROTECT)

    class Meta:
        ordering = ('budget','category',)

    def __str__(self):
        return self.name

class CompensationAccountCategory(models.Model):
    INCOME = 'Rentrées'
    EXPENSE = 'Dépenses'
    TYPES = (
        (INCOME, 'Rentrées'),
        (EXPENSE, 'Dépenses'),
    )

    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200,choices=TYPES)

    def __str__(self):
        return self.name

class AccountingEntry(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    compensation_account = models.ForeignKey('CompensationAccount', on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    name = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name

class ForecastedAccountingEntry(models.Model):
    UNIQUE = 'Unique'
    WEEKLY = 'Hebdomadaire'
    MONTHLY = 'Mensuel'
    QUARTERLY = 'Trimestriel'
    ANNUALLY = 'Annuel'

    TYPES = (
        (UNIQUE, 'Unique'),
        (WEEKLY, 'Hebdomadaire'),
        (MONTHLY, 'Mensuel'),
        (QUARTERLY, 'Trimestriel'),
        (ANNUALLY, 'Annuel'),
    )

    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    compensation_account = models.ForeignKey('CompensationAccount', on_delete=models.CASCADE)
    next_date = models.DateField()
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    name = models.CharField(max_length=200)
    text = models.TextField()
    type = models.CharField(max_length=1,choices=TYPES)

    def __str__(self):
        return self.name
