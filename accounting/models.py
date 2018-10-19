from django.db import models

# Classe représentant un budget. Un utilisateur peut avoir plusieurs budgets et un budget plusieurs utilisateurs.
# Par exemple un utilisateur peut avoir un budget personnel + un budget en commun avec sa compagne, qui a également accès à ce budget.
class Budget(models.Model):
    user = models.ManyToManyField('auth.User')
    name = models.CharField(max_length=200)
    text = models.TextField(default=None, blank=True, null=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name

# Classe représentant un compte.
class Account(models.Model):
    budget = models.ForeignKey('Budget', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.TextField(default=None, blank=True, null=True)
    balance = models.DecimalField(max_digits=13, decimal_places=2)
    type = models.ForeignKey('AccountType', on_delete=models.PROTECT)

    class Meta:
        ordering = ('budget','type',)

    def __str__(self):
        return self.name

# Classe représentant les différents types de compte.
class AccountType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

# Classe représentant les comptes de compensation pour les mouvements entrants et sortants
class CompensationAccount(models.Model):
    budget = models.ForeignKey('Budget', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.TextField(default=None, blank=True, null=True)
    balance = models.DecimalField(max_digits=13, decimal_places=2)
    category = models.ForeignKey('CompensationAccountCategory', on_delete=models.PROTECT)

    class Meta:
        ordering = ('budget','category',)

    def __str__(self):
        return self.name

# Classe représetant les catégorie de compensation, ceci est l'équivalent aux types de compte pour les comptes.
class CompensationAccountCategory(models.Model):
    INCOME = 'Rentrées'
    EXPENSE = 'Dépenses'
    TYPES = (
        (INCOME, 'Rentrées'),
        (EXPENSE, 'Dépenses'),
    )

    parent = models.ForeignKey('self', default=None, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200,choices=TYPES)

    def __str__(self):
        return self.name

# Classe représentant les opérations comptables déjà comptabilisées.
class AccountingEntry(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    counterparty_account = models.ForeignKey('Account', on_delete=models.CASCADE, blank=True, null=True, related_name='accounting_entry_counterparty')
    compensation_account = models.ForeignKey('CompensationAccount', on_delete=models.CASCADE, blank=True, null=True, default=None)
    date = models.DateField()
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    name = models.CharField(max_length=200)
    text = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name

    #Override save method to manage the accounting
    def save(self, *args, **kwargs):
        #Cas de l'ajout d'une nouvelle opération
        if self._state.adding:
            self.account.balance = self.account.balance + self.amount
            self.account.save()
            if self.counterparty_account:
                self.counterparty_account.balance = self.counterparty_account.balance - self.amount
                self.counterparty_account.save()
            else:
                self.compensation_account.balance = self.compensation_account.balance - self.amount
                self.compensation_account.save()

        super().save(*args, **kwargs)

    #Override delete method to manage the accounting
    def delete(self, *args, **kwargs):
        if self.amount != 0:
            self.account.balance = self.account.balance - self.amount
            self.account.save()
            if self.counterparty_account:
                self.counterparty_account.balance = self.counterparty_account.balance + self.amount
                self.counterparty_account.save()
            else:
                self.compensation_account.balance = self.compensation_account.balance + self.amount
                self.compensation_account.save()

        super().delete(*args, **kwargs)

# Classe représentant les opérations comptables plannifiées dans le futur, celles-ci ne sont pas encore comptabilisées.
class PlannedAccountingEntry(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    counterparty_account = models.ForeignKey('Account', on_delete=models.CASCADE, blank=True, null=True, related_name='planned_accounting_entry_counterparty')
    compensation_account = models.ForeignKey('CompensationAccount', on_delete=models.CASCADE, blank=True, null=True, default=None)
    date = models.DateField()
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    name = models.CharField(max_length=200)
    text = models.TextField(default=None, blank=True, null=True)
    recurring_accounting_entry = models.ForeignKey('RecurringAccountingEntry', on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self):
        return self.name

# Classe représentant les opérations comptables réccurentes.
# Un job journalier va alimenter la table des opérations plannifiées à partir de celle-ci.
class RecurringAccountingEntry(models.Model):
    MONTHLY = 'Mensuel'
    QUARTERLY = 'Trimestriel'
    ANNUALLY = 'Annuel'

    TYPES = (
        (MONTHLY, 'Mensuel'),
        (QUARTERLY, 'Trimestriel'),
        (ANNUALLY, 'Annuel')
    )

    type = models.CharField(max_length=1,choices=TYPES)
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    counterparty_account = models.ForeignKey('Account', on_delete=models.CASCADE, blank=True, null=True, related_name='recurring_accounting_entry_counterparty')
    compensation_account = models.ForeignKey('CompensationAccount', on_delete=models.CASCADE, blank=True, null=True, default=None)
    start_date = models.DateField()
    end_date = models.DateField()
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    name = models.CharField(max_length=200)
    text = models.TextField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name
